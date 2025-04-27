from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def admin_list_keyboard(admins: list) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    for admin_id in admins:
        keyboard.add(InlineKeyboardButton(text=f"🆔 {admin_id}", callback_data=f"remove_admin:{admin_id}"))
    keyboard.add(InlineKeyboardButton(text="🔙 بازگشت", callback_data="back_to_admin_panel"))
    return keyboard
