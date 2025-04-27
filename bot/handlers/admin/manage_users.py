from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db, bot
from states import ManageUsers
from filters import AdminFilter
from keyboards import back_keyboard


@dp.message_handler(AdminFilter(), text="➕ افزودن ادمین")
async def add_admin_start(message: types.Message):
    await message.answer("آیدی عددی فرد مورد نظر را ارسال کنید.", reply_markup=back_keyboard)
    await ManageUsers.waiting_for_add_admin.set()


@dp.message_handler(AdminFilter(), text="➖ حذف ادمین")
async def remove_admin_start(message: types.Message):
    await message.answer("آیدی عددی ادمینی که میخواهید حذف کنید را ارسال کنید.", reply_markup=back_keyboard)
    await ManageUsers.waiting_for_remove_admin.set()


@dp.message_handler(AdminFilter(), text="👤 لیست ادمین ها")
async def list_admins(message: types.Message):
    admins = await db.get_admins()
    if not admins:
        await message.answer("هیچ ادمینی ثبت نشده است.", reply_markup=back_keyboard)
        return
    text = "لیست ادمین ها:\n\n"
    text += "\n".join([str(admin_id) for admin_id in admins])
    await message.answer(text, reply_markup=back_keyboard)


@dp.message_handler(state=ManageUsers.waiting_for_add_admin)
async def process_add_admin(message: types.Message, state: FSMContext):
    try:
        admin_id = int(message.text)
    except ValueError:
        await message.answer("آیدی عددی معتبر نیست. لطفاً دوباره تلاش کنید.")
        return
    await db.add_admin(admin_id)
    await message.answer("ادمین با موفقیت اضافه شد.", reply_markup=back_keyboard)
    await state.finish()


@dp.message_handler(state=ManageUsers.waiting_for_remove_admin)
async def process_remove_admin(message: types.Message, state: FSMContext):
    try:
        admin_id = int(message.text)
    except ValueError:
        await message.answer("آیدی عددی معتبر نیست. لطفاً دوباره تلاش کنید.")
        return
    await db.remove_admin(admin_id)
    await message.answer("ادمین با موفقیت حذف شد.", reply_markup=back_keyboard)
    await state.finish()
