from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def file_options(file_id: str):
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text="🗑 حذف فایل", callback_data=f"delete_file:{file_id}"),
        InlineKeyboardButton(text="📈 مشاهده آمار", callback_data=f"file_stats:{file_id}")
    ]
    keyboard.add(*buttons)
    return keyboard
