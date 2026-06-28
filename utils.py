import os

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def is_file(path):
    return os.path.isfile(path)