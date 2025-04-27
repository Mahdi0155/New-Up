from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def user_main_keyboard(channel_username):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("✅ بررسی عضویت", url=f"https://t.me/{channel_username}"),
    )
    return markup
