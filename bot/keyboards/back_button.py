from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_to_menu():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("بازگشت به منو اصلی", callback_data="back_to_main_menu")
    )
    return markup
