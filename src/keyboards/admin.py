from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def admin_panel_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="➕ افزودن ادمین", callback_data="add_admin"),
        InlineKeyboardButton(text="📂 مدیریت فایل‌ها", callback_data="manage_files"),
        InlineKeyboardButton(text="📝 عضویت اجباری", callback_data="manage_channels"),
        InlineKeyboardButton(text="🔙 بازگشت", callback_data="back_to_main")
    )
    return keyboard
