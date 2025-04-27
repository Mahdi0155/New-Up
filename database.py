# src/database.py

admins = set()
files = []

def add_admin(user_id):
    admins.add(user_id)

def remove_admin(user_id):
    admins.discard(user_id)

def list_admins():
    return list(admins)

def add_file(file_id, caption):
    files.append({"file_id": file_id, "caption": caption})

def list_files():
    return files

def delete_file(index):
    if 0 <= index < len(files):
        return files.pop(index)
    return None
