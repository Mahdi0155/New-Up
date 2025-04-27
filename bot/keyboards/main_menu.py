from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        [KeyboardButton("➕ ارسال فایل")]
    ]
    keyboard.add(*sum(buttons, []))
    return keyboard
