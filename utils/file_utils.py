# src/utils/file_utils.py

from database import add_file, list_files, delete_file

def save_file(file_id, caption):
    add_file(file_id, caption)

def get_files():
    return list_files()

def remove_file(index):
    return delete_file(index)
