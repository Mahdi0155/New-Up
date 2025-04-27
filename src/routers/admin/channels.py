from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("channels"))
async def manage_channels(message: Message):
    await message.answer("در این بخش می‌توانید کانال‌های عضویت اجباری را مدیریت کنید.")
