from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def channel_list_keyboard(channels: list) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    for channel in channels:
        keyboard.add(InlineKeyboardButton(text=channel['title'], url=channel['url']))
    keyboard.add(InlineKeyboardButton(text="✅ عضویت انجام شد", callback_data="check_subscription"))
    return keyboard
