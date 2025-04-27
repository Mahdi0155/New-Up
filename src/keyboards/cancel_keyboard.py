from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def cancel_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="❌ لغو", callback_data="cancel"))
    return keyboard
