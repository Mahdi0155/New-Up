from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("channel"))
async def manage_channel(message: Message):
    await message.answer("در این بخش می‌توانید کانال‌های عضویت اجباری را مدیریت کنید.")
