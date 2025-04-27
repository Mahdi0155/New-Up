from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_admin_back():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        [KeyboardButton("🔙 بازگشت به پنل مدیریت")]
    ]
    keyboard.add(*sum(buttons, []))
    return keyboard
