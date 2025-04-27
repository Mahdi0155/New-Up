from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def manage_files_panel():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🗑 حذف فایل", callback_data="delete_file"),
        InlineKeyboardButton("🔙 بازگشت", callback_data="back_to_admin_panel"),
    )
    return keyboard
