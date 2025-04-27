from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_main_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("📂 مدیریت فایل ها", callback_data="manage_files"),
        InlineKeyboardButton("➕ افزودن ادمین", callback_data="add_admin"),
        InlineKeyboardButton("👥 مدیریت ادمین ها", callback_data="manage_admins"),
        InlineKeyboardButton("🔗 عضویت اجباری", callback_data="force_subscription"),
        InlineKeyboardButton("🔙 بازگشت", callback_data="back_to_main")
    )
    return markup
