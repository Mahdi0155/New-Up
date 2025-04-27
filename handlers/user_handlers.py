# src/handlers/user_handlers.py

from aiogram import types, Dispatcher

async def start_handler(message: types.Message):
    await message.answer("خوش آمدید!\nلطفا فایل را ارسال کنید.")

def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"], state="*")
