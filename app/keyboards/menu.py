from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    buttons = [
        [InlineKeyboardButton(text="➕ افزودن فایل جدید", callback_data="add_file")],
        [InlineKeyboardButton(text="📁 مدیریت فایل‌ها", callback_data="manage_files")],
        [InlineKeyboardButton(text="➕ افزودن ادمین جدید", callback_data="add_admin")],
        [InlineKeyboardButton(text="👤 مدیریت ادمین‌ها", callback_data="manage_admins")],
        [InlineKeyboardButton(text="✅ تنظیم عضویت اجباری", callback_data="manage_channels")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def back_button():
    buttons = [
        [InlineKeyboardButton(text="🔙 بازگشت", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
