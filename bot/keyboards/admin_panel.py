from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_main_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("➕ افزودن ادمین", callback_data="add_admin"),
        InlineKeyboardButton("👥 لیست ادمین‌ها", callback_data="list_admins"),
        InlineKeyboardButton("📂 مدیریت فایل‌ها", callback_data="manage_files"),
        InlineKeyboardButton("📢 تنظیم عضویت اجباری", callback_data="set_forced_sub"),
    )
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="admin_back"))
    return markup

def files_manage_keyboard(file_id):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("🗑 حذف فایل", callback_data=f"delete_file:{file_id}")
    )
    markup.add(InlineKeyboardButton("🔙 بازگشت", callback_data="admin_back"))
    return markup

def confirm_upload_keyboard(file_unique_id):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("✅ تایید ارسال", callback_data=f"confirm_send:{file_unique_id}"),
        InlineKeyboardButton("✏️ ویرایش کپشن", callback_data=f"edit_caption:{file_unique_id}")
    )
    return markup
