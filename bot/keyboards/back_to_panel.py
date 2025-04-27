from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_to_panel_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(text="🔙 بازگشت به پنل", callback_data="back_to_panel")
    )
    return keyboard
