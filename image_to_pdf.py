import os

from PIL import Image


NAME_OUT_PDF = "combined.pdf"
allowed_extensions = [".png", "jpg", "jpeg", "bmp"]

def get_file_from_dir(dir_name):
    list_file = []
    for file in os.listdir(dir_name):
        for extension in allowed_extensions:
            if file.endswith(extension):
                list_file.append(os.path.join(dir_name, file))

    return list_file


def create_from_files(list_files, dir_name):
    if list_files:
        first_skip = True
        igm_list = list()
        first_img = Image.open(list_files[0])
        for path_img in list_files:
            if first_skip:
                first_skip = False
                continue

            igm_list.append(Image.open(path_img))
        
        first_img.save(os.path.join(dir_name, NAME_OUT_PDF), "PDF" , resolution=100.0, save_all=True, append_images=igm_list)
