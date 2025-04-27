from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("files"))
async def list_files(message: Message):
    await message.answer("در حال حاضر امکان مشاهده فایل‌ها از طریق پنل مدیریت وجود دارد.")
