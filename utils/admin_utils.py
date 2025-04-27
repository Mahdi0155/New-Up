# src/utils/admin_utils.py

from database import add_admin, remove_admin, list_admins

def is_admin(user_id):
    from config import OWNER_ID
    return user_id == OWNER_ID or user_id in list_admins()

def add_new_admin(user_id):
    add_admin(user_id)

def remove_existing_admin(user_id):
    remove_admin(user_id)

def get_admins_list():
    return list_admins()
