from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.loader import dp, db
from bot.data.config import CHANNEL_ID
from bot.keyboards import main_menu_keyboard


@dp.message_handler(commands=["check_membership"], state="*")
async def check_membership(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    # بررسی عضویت کاربر در کانال
    member = await dp.bot.get_chat_member(CHANNEL_ID, user_id)

    if member.status in ['member', 'administrator', 'creator']:
        await message.answer(
            "شما عضو کانال هستید!\nلطفاً فایل را دریافت کنید.",
            reply_markup=main_menu_keyboard.get_user_main_menu()
        )
    else:
        await message.answer(
            "برای دریافت فایل باید به کانال ملحق شوید.\nلطفاً ابتدا عضو شوید.",
            reply_markup=main_menu_keyboard.get_channel_link_button()
        )
