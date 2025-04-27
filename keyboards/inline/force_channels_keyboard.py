# keyboards/inline/force_channels_keyboard.py

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import db

def force_channels_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    channels = db.get_all_force_channels()
    for ch in channels:
        markup.add(
            InlineKeyboardButton(
                text=f"❌ حذف {ch['title']}",
                callback_data=f"remove_force_channel_{ch['chat_id']}"
            )
        )
    markup.add(
        InlineKeyboardButton(
            text="➕ افزودن کانال جدید",
            callback_data="add_force_channel"
        ),
        InlineKeyboardButton(
            text="🔙 بازگشت",
            callback_data="back_to_admin_panel"
        )
    )
    return markup
