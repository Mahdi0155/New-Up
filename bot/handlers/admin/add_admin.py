from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db
from states.admin_states import AddAdmin
from keyboards.inline.admin_menu import admin_menu_keyboard

@dp.message_handler(commands=["addadmin"], state="*")
async def add_admin_start(message: types.Message):
    await message.answer("لطفاً آیدی عددی ادمین جدید را وارد کنید:")
    await AddAdmin.waiting_for_admin_id.set()

@dp.message_handler(state=AddAdmin.waiting_for_admin_id)
async def add_admin_process(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("آیدی باید فقط عدد باشد. دوباره تلاش کنید:")
        return
    admin_id = int(message.text)
    await db.add_admin(admin_id)
    await message.answer("ادمین جدید با موفقیت اضافه شد.", reply_markup=await admin_menu_keyboard())
    await state.finish()
