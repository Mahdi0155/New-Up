from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.keyboards.manage_files import get_files_list_keyboard, get_back_to_admin_panel_keyboard
from bot.database.database import get_all_files, get_file_by_number, delete_file_by_number
from bot.config import ADMINS

router = Router()

@router.message(F.text == "مدیریت فایل‌ها")
async def manage_files(message: Message):
    if message.from_user.id not in ADMINS:
        return
    files = await get_all_files()
    if not files:
        await message.answer("هیچ فایلی وجود ندارد.", reply_markup=get_back_to_admin_panel_keyboard())
    else:
        await message.answer("لطفا عدد فایل موردنظر را ارسال کنید.", reply_markup=get_files_list_keyboard(files))

@router.message(F.text.regexp(r"^\d+$"))
async def file_action(message: Message, state: FSMContext):
    if message.from_user.id not in ADMINS:
        return
    file_number = int(message.text)
    file = await get_file_by_number(file_number)
    if not file:
        await message.answer("فایلی با این شماره یافت نشد.", reply_markup=get_back_to_admin_panel_keyboard())
        return

    msg = await message.answer(file['text'], reply_markup=get_back_to_admin_panel_keyboard())
    await state.update_data(file_message_id=msg.message_id, file_id=file['id'])

@router.callback_query(F.data == "delete_file")
async def delete_file(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    file_id = data.get("file_id")
    if file_id:
        await delete_file_by_number(file_id)
        await callback.message.answer("فایل با موفقیت حذف شد.", reply_markup=get_back_to_admin_panel_keyboard())
    await callback.answer()
