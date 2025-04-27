from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from data.config import ADMINS
from keyboards.default.admin import admin_panel

@dp.message_handler(text="ارسال پیام همگانی", user_id=ADMINS, state="*")
async def start_broadcast(message: types.Message, state: FSMContext):
    await message.answer("پیام مورد نظر را ارسال کنید:")
    await state.set_state("broadcast_message")

@dp.message_handler(state="broadcast_message", content_types=types.ContentType.TEXT)
async def broadcast_message_handler(message: types.Message, state: FSMContext):
    await state.finish()
    text = message.text
    count = 0
    errors = 0
    users = await get_all_users()  # تابعی که لیست کاربران را میدهد
    for user_id in users:
        try:
            await bot.send_message(chat_id=user_id, text=text)
            count += 1
        except Exception:
            errors += 1
    await message.answer(f"پیام برای {count} کاربر ارسال شد. خطاها: {errors}", reply_markup=admin_panel)

async def get_all_users():
    # این تابع باید از دیتابیس کاربرها را بگیرد
    return []
