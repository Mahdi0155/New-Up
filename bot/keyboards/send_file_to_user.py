from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def send_file_keyboard(file_id: int):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("✅ ارسال", callback_data=f"confirm_send_file:{file_id}"),
        InlineKeyboardButton("❌ لغو", callback_data="cancel_send_file")
    )
    return keyboard
