from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def statistics_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("بازگشت ↩️", callback_data="back_to_main_menu")
    )
    return keyboard
