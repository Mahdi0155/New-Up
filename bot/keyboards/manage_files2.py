from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def manage_files_keyboard(file_id: int):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("🗑 حذف فایل", callback_data=f"delete_file:{file_id}"),
        InlineKeyboardButton("🔙 بازگشت", callback_data="back_to_manage_files"),
    )
    return keyboard
