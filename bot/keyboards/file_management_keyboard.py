from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def file_management_keyboard(file_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.row(
        InlineKeyboardButton(text="✏️ ویرایش کپشن", callback_data=f"edit_caption:{file_id}"),
        InlineKeyboardButton(text="📊 آمار فایل", callback_data=f"file_stats:{file_id}")
    )
    keyboard.row(
        InlineKeyboardButton(text="🗑 حذف فایل", callback_data=f"delete_file:{file_id}"),
        InlineKeyboardButton(text="🔙 بازگشت", callback_data="back_to_file_list")
    )
    return keyboard
