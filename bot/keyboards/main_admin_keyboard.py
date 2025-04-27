from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_admin_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(
        KeyboardButton(text="📁 مدیریت فایل‌ها"),
        KeyboardButton(text="➕ افزودن ادمین")
    )
    keyboard.row(
        KeyboardButton(text="🛡 تنظیمات عضویت اجباری"),
        KeyboardButton(text="🔙 بازگشت")
    )
    return keyboard
