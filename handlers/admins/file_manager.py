from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, db
from states.file_states import ManageFiles
from keyboards.default import admin_panel

@dp.message_handler(text="مدیریت فایل ها", is_admin=True)
async def manage_files_start(message: types.Message):
    await message.answer("لطفاً شماره فایل موردنظر را وارد کنید (عدد):", reply_markup=admin_panel.back_button())
    await ManageFiles.Choosing.set()

@dp.message_handler(state=ManageFiles.Choosing, is_admin=True)
async def show_file_info(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("لطفاً فقط عدد وارد کنید.")
        return
    
    file_number = int(message.text)
    file = await db.get_file_by_number(file_number)
    
    if not file:
        await message.answer("فایلی با این شماره یافت نشد.", reply_markup=admin_panel.back_button())
        return

    await state.update_data(file_id=file['file_id'])
    
    delete_markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton("❌ حذف فایل", callback_data=f"delete_file:{file['file_id']}")
    )
    
    await message.answer(file['caption'], reply_markup=delete_markup)

@dp.callback_query_handler(lambda c: c.data and c.data.startswith('delete_file:'), state=ManageFiles.Choosing, is_admin=True)
async def delete_file_handler(callback_query: types.CallbackQuery, state: FSMContext):
    file_id = callback_query.data.split(":")[1]
    await db.delete_file(file_id)
    
    await callback_query.message.edit_text("✅ فایل با موفقیت حذف شد.")
    await state.finish()
