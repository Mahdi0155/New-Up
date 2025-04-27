from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db
from states.admin import AdminStates
from keyboards.admin import back_button

@dp.message_handler(text="➖ حذف ادمین", state=AdminStates.main)
async def delete_admin_start(message: types.Message, state: FSMContext):
    await message.answer("آیدی عددی ادمینی که میخواهید حذف کنید را ارسال نمایید.", reply_markup=back_button())
    await AdminStates.delete_admin.set()

@dp.message_handler(state=AdminStates.delete_admin)
async def delete_admin_process(message: types.Message, state: FSMContext):
    if message.text == "🔙 بازگشت":
        await message.answer("به پنل مدیریت بازگشتید.", reply_markup=back_button())
        await AdminStates.main.set()
        return
    if not message.text.isdigit():
        await message.answer("آیدی عددی معتبر ارسال کنید.")
        return
    user_id = int(message.text)
    await db.remove_admin(user_id)
    await message.answer(f"✅ کاربر با آیدی `{user_id}` از لیست ادمین‌ها حذف شد.", parse_mode="Markdown")
    await AdminStates.main.set()
