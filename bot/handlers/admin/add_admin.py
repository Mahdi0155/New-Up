from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from filters.admin_only import AdminFilter
from keyboards import admin_panel
from database.admins import add_admin

router = Router()
router.message.filter(AdminFilter())
router.callback_query.filter(AdminFilter())

@router.callback_query(F.data == "add_admin")
async def ask_for_admin_id(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("آیدی عددی فرد موردنظر را ارسال کنید:\n(فقط عدد)", reply_markup=admin_panel.back_to_menu())
    await state.set_state("waiting_for_admin_id")

@router.message(F.text, F.text.regexp(r"^\d+$"))
async def save_admin_id(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == "waiting_for_admin_id":
        user_id = int(message.text)
        success = add_admin(user_id)
        if success:
            await message.answer("✅ ادمین جدید با موفقیت اضافه شد.", reply_markup=admin_panel.menu())
        else:
            await message.answer("⚠️ این کاربر قبلاً ادمین بوده یا خطایی رخ داده.", reply_markup=admin_panel.menu())
        await state.clear()
