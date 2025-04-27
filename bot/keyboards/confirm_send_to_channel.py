from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def confirm_send_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="✅ تایید ارسال", callback_data="confirm_send"),
        InlineKeyboardButton(text="✏️ ویرایش کپشن", callback_data="edit_caption"),
        InlineKeyboardButton(text="🔙 لغو", callback_data="cancel_send")
    )
    return keyboard
