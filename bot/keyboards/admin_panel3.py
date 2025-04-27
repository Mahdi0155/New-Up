from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_main_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("➕ افزودن ادمین", callback_data="add_admin"),
        InlineKeyboardButton("➖ حذف ادمین", callback_data="remove_admin"),
        InlineKeyboardButton("👥 لیست ادمین‌ها", callback_data="list_admins"),
        InlineKeyboardButton("📂 مدیریت فایل‌ها", callback_data="manage_files"),
        InlineKeyboardButton("➕➖ تنظیم عضویت اجباری", callback_data="manage_channels"),
        InlineKeyboardButton("🏠 بازگشت به منو اصلی", callback_data="back_to_main_menu"),
    )
    return markup
