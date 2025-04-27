# src/handlers/common_handlers.py

from aiogram import types, Dispatcher

async def unknown_message(message: types.Message):
    await message.answer("دستور ناشناخته است!")

def register_common_handlers(dp: Dispatcher):
    dp.register_message_handler(unknown_message)
