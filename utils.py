import os
from PIL import Image
 
# 读取目录下所有匹配文件
def read_dictionary(folder, keys):
    images = []
    for file_name in os.listdir(folder):
        flag = False
        for key in keys:
            if file_name.find(key) > -1:
                flag = True
        if flag:
            image = Image.open(folder + "/" + file_name)
            images.append(image)
    return images
  
# 删除目录下所有文件
def del_dictionary_file(folder):
    del_list = os.listdir(folder)
    for f in del_list:
        file_path = os.path.join(folder, f)
        if os.path.isfile(file_path):
            os.remove(file_path)

def make_sprites(name,keys = [],ignoreStr=''):
    folderPath = "./resize&group"
    resultPath = "./css-sprites"
    if not os.path.exists(resultPath):
        os.makedirs(resultPath)
    # 读取文件夹下的所有图片
    images = []  # 图片
    imagesName = []
    images = read_dictionary(folderPath,keys)
    for root, dirs, files in os.walk(folderPath):
        for file_name in files:
            flag = False
            for key in keys:
                if file_name.find(key) > -1:
                    flag = True
            if flag:
                imagesName.append(file_name)
    for i in range(len(imagesName)):
        imagesName[i] = os.path.split(imagesName[i])[1]
        imagesName[i] = os.path.splitext(imagesName[i])[0]
    # 设置css sprite图片相关参数
    # print("css sprite相关参数:")
    p = pow(len(images), 0.5)
    row = int(p) + 1
    column = int(p)
    # zoom = input("图片缩放大小（倍数）:")
    # if zoom == "":
    zoom = "0.5"
    zoom = float(zoom)
    # 个性化配置
    # ignoreStr = input("需要忽略的文件中的字符串:")

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
    resultImg.save(resultPath + '/' + name + '_' + str(zoom) + ".png")  # 写入图片
    # 写入json
    styleFile = open(resultPath + '/' + name + '_' + str(zoom) + ".json", "w")
    styleFile.write(resultStyle)
    styleFile.close()