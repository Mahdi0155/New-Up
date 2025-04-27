from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.database.database import get_all_files, delete_file_by_id
from bot.keyboards.manage_files import generate_files_list_keyboard
from bot.keyboards.back import back_to_admin_panel

router = Router()

@router.callback_query(lambda c: c.data == 'manage_files')
async def manage_files_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state("awaiting_file_number")
    files = await get_all_files()
    if not files:
        await callback_query.message.answer("هیچ فایلی برای مدیریت وجود ندارد.", reply_markup=back_to_admin_panel())
        return
    await callback_query.message.answer("لطفاً شماره فایلی که میخواهید مدیریت کنید را وارد کنید:",
                                        reply_markup=generate_files_list_keyboard(files))


@router.message(lambda message: message.text.isdigit())
async def file_number_received(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state != "awaiting_file_number":
        return
    file_number = int(message.text)
    files = await get_all_files()
    if file_number < 1 or file_number > len(files):
        await message.answer("شماره فایل معتبر نیست.", reply_markup=back_to_admin_panel())
        return

    selected_file = files[file_number - 1]
    file_id, file_type, caption = selected_file

    if file_type == 'photo':
        await message.answer_photo(file_id, caption=caption,
                                   reply_markup=types.InlineKeyboardMarkup(
                                       inline_keyboard=[
                                           [types.InlineKeyboardButton(text="❌ حذف فایل", callback_data=f"delete_file:{file_id}")],
                                           [types.InlineKeyboardButton(text="🔙 بازگشت", callback_data="back_to_manage_files")]
                                       ]
                                   ))
    elif file_type == 'video':
        await message.answer_video(file_id, caption=caption,
                                   reply_markup=types.InlineKeyboardMarkup(
                                       inline_keyboard=[
                                           [types.InlineKeyboardButton(text="❌ حذف فایل", callback_data=f"delete_file:{file_id}")],
                                           [types.InlineKeyboardButton(text="🔙 بازگشت", callback_data="back_to_manage_files")]
                                       ]
                                   ))

    await state.clear()

@router.callback_query(lambda c: c.data and c.data.startswith('delete_file:'))
async def delete_file_handler(callback_query: CallbackQuery):
    file_id = callback_query.data.split(":")[1]
    await delete_file_by_id(file_id)
    await callback_query.message.edit_text("فایل با موفقیت حذف شد.", reply_markup=back_to_admin_panel())
