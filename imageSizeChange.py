from PIL import Image
import os

from utils import del_dictionary_file

# 统一至指定图片大小
# 居中、裁剪、缩放
scaleSize = 1
width = 512
height = 512

def img_size_change(source_folder : str, destination_folder : str):
    del_dictionary_file(destination_folder)
    # iterate over all files in source folder
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            out_file_path = os.path.join(destination_folder, file_name)
            im = Image.open(file_path)
            if file_name.find('uniequip') > -1 or file_name.find('default') > -1 :
                box = ((im.size[0] - 512) / 2, (im.size[1] - 512) / 2 , im.size[0] - (im.size[0] - 512) / 2, im.size[1] - (im.size[1] - 512) / 2 )
                region = im.crop(box)
                region.save(out_file_path)
            else:
                im.save(out_file_path)
# img_size_change('destination','resize&group')