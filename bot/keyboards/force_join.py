from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def force_join_panel():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("➕ افزودن کانال", callback_data="add_channel"),
        InlineKeyboardButton("➖ حذف کانال", callback_data="remove_channel"),
        InlineKeyboardButton("📜 لیست کانال‌ها", callback_data="list_channels"),
        InlineKeyboardButton("🔙 بازگشت", callback_data="back_to_admin_panel"),
    )
    return keyboard
