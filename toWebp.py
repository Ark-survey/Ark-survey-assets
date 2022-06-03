import os
import tinify
from threading import Thread

tinify.key = "vMsNmcZQljq5RN9RfxSsJwsbW0LXrnkl"

def main(root,file_name,source_folder):
    for i in range(2):
        file_path = os.path.join(root, file_name)
        print(file_path)
        out_file_path = os.path.join(source_folder, file_name.replace('.png', '.webp'))
        source = tinify.from_file(file_path)
        source.to_file(out_file_path)

def to_webp(source_folder : str):
    # iterate over all files in source folder
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            if file_name.find('.png') > -1:
                thread = Thread(target=main, args=(root,file_name,source_folder))
                thread.start()