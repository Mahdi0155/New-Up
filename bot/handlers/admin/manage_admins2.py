from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp, db
from states.admin_states import ManageAdmins
from utils.keyboards import back_to_admin_panel

@dp.message_handler(Text(equals="➕ افزودن ادمین"), state="*")
async def add_admin(message: types.Message):
    await message.answer("آیدی عددی فرد مورد نظر را ارسال کنید:", reply_markup=back_to_admin_panel())
    await ManageAdmins.waiting_for_admin_id.set()

@dp.message_handler(state=ManageAdmins.waiting_for_admin_id)
async def save_admin_id(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("لطفاً فقط آیدی عددی ارسال کنید.")
        return
    admin_id = int(message.text)
    if await db.add_admin(admin_id):
        await message.answer(f"✅ ادمین جدید با موفقیت اضافه شد: {admin_id}")
    else:
        await message.answer("این آیدی قبلاً به عنوان ادمین ثبت شده.")
    await state.finish()

@dp.message_handler(Text(equals="➖ حذف ادمین"), state="*")
async def remove_admin(message: types.Message):
    await message.answer("آیدی عددی ادمینی که میخواید حذف کنید را ارسال کنید:", reply_markup=back_to_admin_panel())
    await ManageAdmins.waiting_for_admin_remove.set()

@dp.message_handler(state=ManageAdmins.waiting_for_admin_remove)
async def delete_admin_id(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("لطفاً فقط آیدی عددی ارسال کنید.")
        return
    admin_id = int(message.text)
    if await db.remove_admin(admin_id):
        await message.answer(f"✅ ادمین {admin_id} با موفقیت حذف شد.")
    else:
        await message.answer("این آیدی به عنوان ادمین ثبت نشده.")
    await state.finish()
