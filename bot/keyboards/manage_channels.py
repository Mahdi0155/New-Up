from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def manage_channels_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("➕ اضافه کردن کانال", callback_data="add_channel"),
        InlineKeyboardButton("➖ حذف کردن کانال", callback_data="remove_channel"),
        InlineKeyboardButton("📃 لیست کانال ها", callback_data="list_channels"),
        InlineKeyboardButton("🔙 بازگشت", callback_data="back_to_admin_panel")
    )
    return keyboard
