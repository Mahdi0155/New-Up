from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_admin_panel():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("➕ افزودن ادمین", callback_data="add_admin"),
        InlineKeyboardButton("📋 لیست ادمین‌ها", callback_data="list_admins"),
    )
    keyboard.add(
        InlineKeyboardButton("📁 مدیریت فایل‌ها", callback_data="manage_files"),
        InlineKeyboardButton("🛡 تنظیمات عضویت اجباری", callback_data="force_subscription"),
    )
    keyboard.add(
        InlineKeyboardButton("🔙 بازگشت", callback_data="back_to_menu")
    )
    return keyboard
