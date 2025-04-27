from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def manage_files_keyboard(file_id: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="🗑️ حذف فایل", callback_data=f"delete_file:{file_id}"),
        InlineKeyboardButton(text="🔙 برگشت", callback_data="back_to_manage_files")
    )
    return keyboard
