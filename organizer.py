
import os
import shutil
from config import FILE_TYPES
from logger import log_message
from utils import create_folder, is_file


def get_files(folder_path):
    return os.listdir(folder_path)


def get_category(file_name):
    extension = os.path.splitext(file_name)[1].lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_filename(destination_folder, file_name):
    """
    Returns a unique filename if the file already exists.
    Example:
        resume.pdf
        resume(1).pdf
        resume(2).pdf
    """

    name, extension = os.path.splitext(file_name)

    counter = 1
    new_file_name = file_name

    while os.path.exists(os.path.join(destination_folder, new_file_name)):
        new_file_name = f"{name}({counter}){extension}"
        counter += 1

    return new_file_name


def organize_files(folder_path):
    files = get_files(folder_path)

    for file in files:

        source = os.path.join(folder_path, file)

        # Skip folders
        if not is_file(source):
            continue

        category = get_category(file)

        destination_folder = os.path.join(folder_path, category)

        # Create destination folder
        create_folder(destination_folder)

        # Handle duplicate filenames
        unique_file = get_unique_filename(destination_folder, file)

        destination = os.path.join(destination_folder, unique_file)

        try:
            shutil.move(source, destination)

            message = f"{file} -> {category}/{unique_file}"

            print(message)

            log_message(message)

        except Exception as e:
            print(f"Error moving {file}: {e}")
            log_message(f"ERROR: {file} - {e}")


def organize_by_size(folder_path):
    files = get_files(folder_path)

    for file in files:

        source = os.path.join(folder_path, file)

        # Skip folders
        if not is_file(source):
            continue

        size = os.path.getsize(source)

        if size < 1024 * 1024:
            folder = "Small Files"

        elif size < 10 * 1024 * 1024:
            folder = "Medium Files"

        else:
            folder = "Large Files"

        destination_folder = os.path.join(folder_path, folder)

        create_folder(destination_folder)

        unique_file = get_unique_filename(destination_folder, file)

        destination = os.path.join(destination_folder, unique_file)

        try:
            shutil.move(source, destination)

            message = f"{file} -> {folder}/{unique_file}"

            print(message)

            log_message(message)

        except Exception as e:
            print(f"Error moving {file}: {e}")
            log_message(f"ERROR: {file} - {e}")