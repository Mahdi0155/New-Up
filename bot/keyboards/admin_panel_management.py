from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def manage_admins_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="➕ افزودن ادمین جدید", callback_data="add_admin"),
        InlineKeyboardButton(text="➖ حذف ادمین", callback_data="remove_admin"),
        InlineKeyboardButton(text="🔙 برگشت", callback_data="back_to_admin_panel")
    )
    return keyboard
