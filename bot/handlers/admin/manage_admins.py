from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp, db
from states.admin import AdminStates
from keyboards.default.admin import manage_admins_keyboard, back_to_admin_panel_keyboard


@dp.message_handler(text="👤 مدیریت ادمین ها", state="*")
async def manage_admins_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("لطفا یک گزینه را انتخاب کنید:", reply_markup=manage_admins_keyboard())


@dp.message_handler(text="➕ افزودن ادمین جدید", state="*")
async def add_admin_handler(message: types.Message):
    await message.answer("لطفا آیدی عددی ادمین جدید را ارسال کنید:", reply_markup=back_to_admin_panel_keyboard())
    await AdminStates.waiting_for_admin_id.set()


@dp.message_handler(state=AdminStates.waiting_for_admin_id)
async def save_admin_handler(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("آیدی باید عددی باشد. لطفا دوباره ارسال کنید.")
        return
    admin_id = int(message.text)
    db.add_admin(admin_id)
    await message.answer("ادمین با موفقیت اضافه شد.", reply_markup=manage_admins_keyboard())
    await state.finish()


@dp.message_handler(text="➖ حذف ادمین", state="*")
async def delete_admin_handler(message: types.Message):
    admins = db.get_admins()
    if not admins:
        await message.answer("ادمینی وجود ندارد.", reply_markup=manage_admins_keyboard())
        return
    text = "آیدی ادمین‌هایی که می‌توانید حذف کنید:\n\n"
    text += "\n".join(str(admin) for admin in admins)
    await message.answer(text, reply_markup=back_to_admin_panel_keyboard())
    await AdminStates.waiting_for_admin_id_to_delete.set()


@dp.message_handler(state=AdminStates.waiting_for_admin_id_to_delete)
async def remove_admin_handler(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("آیدی باید عددی باشد. لطفا دوباره ارسال کنید.")
        return
    admin_id = int(message.text)
    db.remove_admin(admin_id)
    await message.answer("ادمین با موفقیت حذف شد.", reply_markup=manage_admins_keyboard())
    await state.finish()
