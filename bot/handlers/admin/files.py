from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.database.database import Database
from bot.keyboards.manage_files import files_list_keyboard
from bot.keyboards.confirm_delete import confirm_delete_keyboard
from bot.states.files import FileManagement

router = Router()

@router.message(Command("manage_files"))
async def manage_files(message: types.Message, state: FSMContext):
    await message.answer("لطفاً شماره فایل رو وارد کن:", reply_markup=files_list_keyboard())
    await state.set_state(FileManagement.select_file)

@router.message(FileManagement.select_file)
async def selected_file(message: types.Message, state: FSMContext):
    file_number = message.text.strip()
    file_data = Database.get_file_by_number(file_number)
    if file_data:
        await state.update_data(file_id=file_data["file_id"])
        await message.answer_document(file_data["file_id"], caption=file_data["caption"], reply_markup=confirm_delete_keyboard())
        await state.set_state(FileManagement.confirm_delete)
    else:
        await message.answer("فایل پیدا نشد! لطفاً یک شماره‌ی صحیح وارد کن.")

@router.callback_query(FileManagement.confirm_delete, F.data == "confirm_delete")
async def confirm_delete(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    file_id = data.get("file_id")
    if file_id:
        Database.delete_file(file_id)
        await callback.message.edit_text("فایل با موفقیت حذف شد.")
    else:
        await callback.message.edit_text("خطا در حذف فایل!")
    await state.clear()
