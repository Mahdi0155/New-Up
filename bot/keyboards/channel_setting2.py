from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def channels_setting_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ افزودن کانال", callback_data="add_channel"),
            InlineKeyboardButton(text="➖ حذف کانال", callback_data="remove_channel")
        ],
        [
            InlineKeyboardButton(text="🔙 برگشت", callback_data="back_to_main")
        ]
    ])
    return keyboard
