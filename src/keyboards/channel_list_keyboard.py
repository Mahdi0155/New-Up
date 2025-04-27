from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def channel_list_keyboard(channels: list) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    for channel in channels:
        keyboard.add(InlineKeyboardButton(text=f"{channel['name']}", url=channel['url']))
    keyboard.add(InlineKeyboardButton(text="➕ اضافه کردن کانال", callback_data="add_channel"))
    keyboard.add(InlineKeyboardButton(text="🔙 بازگشت", callback_data="back_to_admin_panel"))
    return keyboard
