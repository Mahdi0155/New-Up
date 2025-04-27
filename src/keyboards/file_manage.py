from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def file_list_keyboard(file_count: int) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=5)
    for i in range(1, file_count + 1):
        keyboard.insert(InlineKeyboardButton(text=str(i), callback_data=f"file_{i}"))
    keyboard.add(InlineKeyboardButton(text="🔙 بازگشت", callback_data="back_to_admin"))
    return keyboard

def file_action_keyboard(file_id: int) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="🗑 حذف فایل", callback_data=f"delete_file_{file_id}"),
        InlineKeyboardButton(text="🔙 بازگشت", callback_data="back_to_file_list")
    )
    return keyboard
