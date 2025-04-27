from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from bot.keyboards import manage_admins
from bot.database import admins

router = Router()

@router.message(Command("add_admin"))
async def add_admin_handler(message: Message):
    if not await admins.is_super_admin(message.from_user.id):
        return
    await message.answer("ایدی عددی ادمین جدید را ارسال کنید:")

@router.message(F.text.isdigit())
async def save_admin(message: Message):
    if not await admins.is_super_admin(message.from_user.id):
        return
    admin_id = int(message.text)
    await admins.add_admin(admin_id)
    await message.answer("ادمین جدید اضافه شد.", reply_markup=manage_admins.back_to_panel())
