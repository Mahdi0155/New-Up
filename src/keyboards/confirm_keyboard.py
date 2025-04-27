from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def confirm_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="✅ تایید", callback_data="confirm"),
        InlineKeyboardButton(text="❌ لغو", callback_data="cancel")
    )
    return keyboard
