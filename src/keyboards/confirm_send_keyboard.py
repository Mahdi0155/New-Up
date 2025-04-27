from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def confirm_send_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="✅ تایید ارسال", callback_data="confirm_send"),
        InlineKeyboardButton(text="✏️ ویرایش کپشن", callback_data="edit_caption")
    )
    return keyboard
