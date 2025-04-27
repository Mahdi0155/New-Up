from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db
from states.admin import AdminStates
from keyboards.admin import back_button

@dp.message_handler(text="👤 مشاهده ادمین‌ها", state=AdminStates.main)
async def view_admins(message: types.Message, state: FSMContext):
    admins = await db.get_admins()
    if not admins:
        await message.answer("هیچ ادمینی ثبت نشده است.", reply_markup=back_button())
        return
    text = "لیست ادمین‌ها:\n\n"
    for admin_id in admins:
        text += f"• `{admin_id}`\n"
    await message.answer(text, parse_mode="Markdown", reply_markup=back_button())
