from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_panel():
    buttons = [
        [InlineKeyboardButton(text="➕ افزودن ادمین", callback_data="add_admin")],
        [InlineKeyboardButton(text="➖ حذف ادمین", callback_data="remove_admin")],
        [InlineKeyboardButton(text="📋 لیست ادمین‌ها", callback_data="list_admins")],
        [InlineKeyboardButton(text="🔙 بازگشت", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def confirm_admin_addition(user_id: int):
    buttons = [
        [
            InlineKeyboardButton(text="✅ تایید افزودن", callback_data=f"confirm_add_admin:{user_id}"),
            InlineKeyboardButton(text="❌ لغو", callback_data="cancel_add_admin")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def confirm_admin_removal(user_id: int):
    buttons = [
        [
            InlineKeyboardButton(text="✅ تایید حذف", callback_data=f"confirm_remove_admin:{user_id}"),
            InlineKeyboardButton(text="❌ لغو", callback_data="cancel_remove_admin")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
