from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db
from states.admin import AdminStates
from keyboards.admin import back_button

@dp.message_handler(text="➕ افزودن ادمین", state=AdminStates.main)
async def add_admin_start(message: types.Message, state: FSMContext):
    await message.answer("لطفا آیدی عددی ادمین جدید را ارسال کنید.", reply_markup=back_button())
    await AdminStates.add_admin.set()

@dp.message_handler(state=AdminStates.add_admin)
async def add_admin_process(message: types.Message, state: FSMContext):
    if message.text == "🔙 بازگشت":
        await message.answer("به پنل مدیریت بازگشتید.", reply_markup=back_button())
        await AdminStates.main.set()
        return
    if not message.text.isdigit():
        await message.answer("آیدی عددی معتبر ارسال کنید.")
        return
    user_id = int(message.text)
    await db.add_admin(user_id)
    await message.answer(f"✅ کاربر با آیدی `{user_id}` به لیست ادمین‌ها اضافه شد.", parse_mode="Markdown")
    await AdminStates.main.set()
