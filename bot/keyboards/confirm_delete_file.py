from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def confirm_delete_file_keyboard(file_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="✅ تایید حذف", callback_data=f"confirm_delete:{file_id}"),
        InlineKeyboardButton(text="❌ انصراف", callback_data="cancel_delete")
    )
    return keyboard
