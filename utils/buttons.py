from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_admin_buttons():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("➕ افزودن ادمین", callback_data="add_admin"),
        InlineKeyboardButton("➖ حذف ادمین", callback_data="remove_admin"),
        InlineKeyboardButton("🗂 مدیریت فایل‌ها", callback_data="manage_files"),
        InlineKeyboardButton("➕➖ عضویت اجباری", callback_data="manage_channels"),
        InlineKeyboardButton("🔙 بازگشت", callback_data="back_main"),
    )
    return keyboard

def file_manage_buttons(file_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("🗑 حذف فایل", callback_data=f"delete_file:{file_id}")
    )
    keyboard.add(
        InlineKeyboardButton("🔙 بازگشت", callback_data="back_main")
    )
    return keyboard

def confirm_upload_buttons(file_id):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("✅ تایید ارسال", callback_data=f"confirm_send:{file_id}"),
        InlineKeyboardButton("✏️ ویرایش کپشن", callback_data=f"edit_caption:{file_id}")
    )
    return keyboard

def join_channel_button(url):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("عضویت در کانال", url=url)
    )
    keyboard.add(
        InlineKeyboardButton("بررسی عضویت", callback_data="check_subscription")
    )
    return keyboard
