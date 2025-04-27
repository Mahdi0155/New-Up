from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def confirm_send_file_keyboard(file_id: str) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="✅ تایید ارسال", callback_data=f"confirm_send:{file_id}"),
        InlineKeyboardButton(text="✏️ ویرایش کپشن", callback_data=f"edit_caption:{file_id}")
    )
    return keyboard
