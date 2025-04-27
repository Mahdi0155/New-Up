from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db
from states.file_states import ManageFiles
from keyboards.default import admin_panel

@dp.message_handler(text="مدیریت فایل‌ها", is_admin=True)
async def manage_files(message: types.Message):
    total_files = await db.get_files_count()
    if total_files == 0:
        await message.answer("هیچ فایلی برای مدیریت وجود ندارد.", reply_markup=admin_panel.back_button())
    else:
        await message.answer(f"تعداد کل فایل‌ها: {total_files}\n\nعدد فایل مورد نظر را ارسال کنید (از 1 تا {total_files})", reply_markup=admin_panel.back_button())
        await ManageFiles.Choosing.set()

@dp.message_handler(state=ManageFiles.Choosing)
async def choose_file(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("لطفاً یک عدد معتبر ارسال کنید.")
        return
    
    file_number = int(message.text)
    total_files = await db.get_files_count()

    if file_number < 1 or file_number > total_files:
        await message.answer("عدد وارد شده خارج از محدوده است.")
        return

    file = await db.get_file_by_index(file_number)
    
    if not file:
        await message.answer("فایل پیدا نشد.")
        await state.finish()
        return

    # ارسال فایل به همراه دکمه حذف
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="❌ حذف فایل", callback_data=f"delete_file:{file['file_id']}"))

    await message.answer(file['caption'], reply_markup=markup)
    await state.finish()

@dp.callback_query_handler(lambda c: c.data.startswith("delete_file:"))
async def delete_file(callback_query: types.CallbackQuery):
    file_id = callback_query.data.split(":")[1]
    await db.delete_file(file_id)
    await callback_query.message.edit_text("✅ فایل با موفقیت حذف شد.")
    await callback_query.answer()
