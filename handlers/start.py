from aiogram import Router, F
from aiogram.types import Message
from keyboards import main_admin_keyboard, main_user_keyboard
from middlewares import is_admin
from config import ADMINS

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    user_id = message.from_user.id
    if str(user_id) in ADMINS:
        await message.answer(
            "سلام ادمین عزیز!\nبه پنل مدیریت خوش اومدی.",
            reply_markup=main_admin_keyboard()
        )
    else:
        await message.answer(
            "سلام خوش اومدی!\nجهت دریافت فایل لطفاً عضو کانال شو و روی دکمه بررسی عضویت کلیک کن.",
            reply_markup=main_user_keyboard()
        )
