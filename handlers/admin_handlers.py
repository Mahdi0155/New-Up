# src/handlers/admin_handlers.py

from aiogram import types, Dispatcher
from config import OWNER_ID
from utils.admin_utils import is_admin

async def admin_panel(message: types.Message):
    if not is_admin(message.from_user.id):
        return
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["➕ افزودن ادمین", "➖ حذف ادمین", "📂 مدیریت فایل‌ها", "⚙️ عضویت اجباری", "🔙 بازگشت"]
    keyboard.add(*buttons)
    await message.answer("به پنل مدیریت خوش آمدید.", reply_markup=keyboard)

def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_panel, commands=["admin"], state="*")
