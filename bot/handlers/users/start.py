from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.loader import dp, db
from bot.keyboards import main_menu_keyboard
from bot.data.config import ADMINS


@dp.message_handler(commands=["start"], state="*")
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()

    if message.from_user.id in ADMINS:
        await message.answer(
            "به پنل مدیریت خوش آمدید!",
            reply_markup=main_menu_keyboard.get_admin_main_menu()
        )
    else:
        await message.answer(
            "به ربات خوش آمدید!\n\nبرای دریافت فایل، عضویت خود را بررسی کنید.",
            reply_markup=main_menu_keyboard.get_user_main_menu()
        )
