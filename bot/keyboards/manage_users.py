from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def manage_users_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("➕ اضافه کردن ادمین", callback_data="add_admin"),
        InlineKeyboardButton("➖ حذف کردن ادمین", callback_data="remove_admin"),
        InlineKeyboardButton("📃 لیست ادمین ها", callback_data="list_admins"),
        InlineKeyboardButton("🔙 بازگشت", callback_data="back_to_admin_panel")
    )
    return keyboard
