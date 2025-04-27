from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def manage_forced_subscription():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➕ افزودن کانال اجباری", callback_data="add_forced_channel")],
        [InlineKeyboardButton(text="➖ حذف کانال اجباری", callback_data="remove_forced_channel")],
        [InlineKeyboardButton(text="🔙 بازگشت به مدیریت", callback_data="back_to_admin_panel")]
    ])
    return keyboard
