from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("files"))
async def manage_files(message: Message):
    await message.answer("در این قسمت می‌توانید فایل‌های ذخیره شده را مدیریت کنید.")
