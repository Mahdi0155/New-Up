from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def file_actions(file_id: str):
    buttons = [
        [InlineKeyboardButton(text="❌ حذف فایل", callback_data=f"delete_file:{file_id}")],
        [InlineKeyboardButton(text="✏️ ویرایش کپشن", callback_data=f"edit_caption:{file_id}")],
        [InlineKeyboardButton(text="📊 مشاهده آمار", callback_data=f"file_stats:{file_id}")],
        [InlineKeyboardButton(text="📤 ارسال به دوست", switch_inline_query=file_id)],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def confirm_deletion(file_id: str):
    buttons = [
        [
            InlineKeyboardButton(text="✅ تایید حذف", callback_data=f"confirm_delete:{file_id}"),
            InlineKeyboardButton(text="❌ لغو", callback_data="cancel_delete")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
