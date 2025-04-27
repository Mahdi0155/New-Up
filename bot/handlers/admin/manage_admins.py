from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp, db, bot
from states import AddAdmin, RemoveAdmin
from filters import IsMainAdmin
from utils import get_admins_keyboard

@dp.message_handler(IsMainAdmin(), text="➕ اضافه کردن ادمین")
async def add_admin_handler(message: types.Message):
    await message.answer("لطفا آیدی عددی ادمین جدید را ارسال کنید:")
    await AddAdmin.waiting_for_admin_id.set()

@dp.message_handler(state=AddAdmin.waiting_for_admin_id)
async def save_new_admin(message: types.Message, state: FSMContext):
    admin_id = message.text.strip()
    if not admin_id.isdigit():
        await message.answer("آیدی نامعتبر است. فقط عدد ارسال کنید.")
        return
    await db.add_admin(int(admin_id))
    await message.answer("✅ ادمین جدید اضافه شد.")
    await state.finish()

@dp.message_handler(IsMainAdmin(), text="➖ حذف ادمین")
async def remove_admin_handler(message: types.Message):
    admins = await db.get_admins()
    if not admins:
        await message.answer("هیچ ادمینی ثبت نشده است.")
        return
    keyboard = await get_admins_keyboard(admins)
    await message.answer("ادمینی که میخواهید حذف کنید را انتخاب کنید:", reply_markup=keyboard)
    await RemoveAdmin.waiting_for_admin_id.set()

@dp.callback_query_handler(state=RemoveAdmin.waiting_for_admin_id)
async def confirm_remove_admin(call: types.CallbackQuery, state: FSMContext):
    admin_id = call.data
    await db.remove_admin(int(admin_id))
    await call.message.edit_text("✅ ادمین حذف شد.")
    await state.finish()
