from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("admins"))
async def manage_admins(message: Message):
    await message.answer("در این بخش می‌توانید ادمین‌های ربات را مدیریت کنید.")
