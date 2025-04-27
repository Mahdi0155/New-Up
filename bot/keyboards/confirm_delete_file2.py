from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def confirm_delete_file(file_id: int):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ تایید حذف", callback_data=f"confirm_delete_file:{file_id}"),
            InlineKeyboardButton(text="❌ لغو", callback_data="cancel_delete_file")
        ]
    ])
    return keyboard
