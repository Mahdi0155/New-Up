from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_admin_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        [KeyboardButton("➕ افزودن فایل")],
        [KeyboardButton("📂 مدیریت فایل‌ها")],
        [KeyboardButton("👤 مدیریت ادمین‌ها")],
        [KeyboardButton("🛡️ عضویت اجباری")],
        [KeyboardButton("🔙 بازگشت")]
    ]
    keyboard.add(*sum(buttons, []))
    return keyboard
