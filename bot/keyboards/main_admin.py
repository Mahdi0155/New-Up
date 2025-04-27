from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_admin():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        [KeyboardButton("➕ اپلود فایل جدید")],
        [KeyboardButton("📂 مدیریت فایل‌ها")],
        [KeyboardButton("➕ افزودن ادمین")],
        [KeyboardButton("👥 مدیریت عضویت اجباری")],
        [KeyboardButton("🔙 بازگشت")]
    ]
    keyboard.add(*sum(buttons, []))
    return keyboard
