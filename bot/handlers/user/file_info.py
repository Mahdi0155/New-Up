from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db

@dp.callback_query_handler(lambda c: c.data and c.data.startswith("file_info:"))
async def file_info_handler(callback_query: types.CallbackQuery, state: FSMContext):
    file_id = int(callback_query.data.split(":")[1])
    file = db.get_file(file_id)

    if not file:
        await callback_query.answer("فایل پیدا نشد.", show_alert=True)
        return

    text = f"اطلاعات فایل:\n\n"
    text += f"آیدی فایل: {file_id}\n"
    text += f"نوع: {file['type']}\n"
    text += f"تعداد دریافت: {file['downloads']}\n"
    text += f"تاریخ ثبت: {file['created_at']}"

    await callback_query.message.answer(text)
    await callback_query.answer()
