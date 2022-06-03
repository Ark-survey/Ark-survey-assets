from operator import length_hint
import os
from PIL import Image
from utils import read_dictionary

# 文件位置读取
folderPath = input("请输入图片位置:")
if folderPath == "":
    folderPath = "./images"
resultPath = input("请输入生成位置:")
if resultPath == "":
    resultPath = "./result"
if not os.path.exists(resultPath):
    os.makedirs(resultPath)
# 读取文件夹下的所有图片
images = []  # 图片
images = read_dictionary(folderPath)
imagesName = os.listdir(folderPath)
for i in range(len(imagesName)):
    imagesName[i] = os.path.split(imagesName[i])[1]
    imagesName[i] = os.path.splitext(imagesName[i])[0]
print("当前目录下一共有" + str(len(images)) + "张图片")
# 设置css sprite图片相关参数
print("css sprite相关参数:")
p = pow(len(images), 0.5)
row = int(p) + 1
column = int(p)
zoom = input("图片缩放大小（倍数）:")
if zoom == "":
    zoom = "1"
zoom = float(zoom)
# 个性化配置
ignoreStr = input("需要忽略的文件中的字符串:")

# 计算css sprite大小
totalSize = (images[0].size[0] * column, images[0].size[1] * row)
resultImg = Image.new("RGBA", (int(totalSize[0] * zoom), int(totalSize[1] * zoom)), (0, 0, 0, 0))
resultStyle = "{\n"
# 获取图片高宽（每张图应该一致）
singleWidth = int(images[0].size[0] * zoom)
singleHeight = int(images[0].size[1] * zoom)
# 生成css sprite
widthPos = 0
heightPos = 0
i = -1

for image in images:
    i = i + 1
    # 添加图片
    image = image.resize((int(image.size[0] * zoom), int(image.size[1] * zoom)))
    resultImg.paste(image, (widthPos, heightPos, widthPos + image.size[0], heightPos + image.size[1]))
    # 添加对应scss样式
    imagesName[i] = imagesName[i].replace(ignoreStr, "")
    # [x]改为_x，防止css样式问题
    imagesName[i] = imagesName[i].replace("[", "_")
    imagesName[i] = imagesName[i].replace("]", "")
    resultStyle += "\t\"" + imagesName[i] + "\": [" + str(widthPos * -1) + "," + str(heightPos * -1)
    # 切换到下一张图片
    widthPos += image.size[0]
    if i % column == column - 1:
        heightPos += singleHeight
        widthPos = 0
    if i < len(images) - 1:
      resultStyle += "],\n"
    else:
      resultStyle += "]\n"
resultStyle += "}"
resultImg.save(resultPath + '_' + str(zoom) + ".png")  # 写入图片
# 写入json
styleFile = open(resultPath + '_' + str(zoom) + ".json", "w")
styleFile.write(resultStyle)
styleFile.close()
