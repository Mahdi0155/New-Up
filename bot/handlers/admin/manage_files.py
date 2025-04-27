from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext

from bot.database.database import Database
from bot.keyboards.manage_files import get_files_keyboard
from bot.keyboards.manage_files import back_keyboard
from bot.states.manage_files import ManageFiles
from bot.utils.get_file_message import get_file_message
from bot.utils.delete_file import delete_file

router = Router()
db = Database()

@router.callback_query(F.data == "manage_files")
async def manage_files(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    files_count = await db.count_files()
    if files_count == 0:
        await callback.message.edit_text("هیچ فایلی موجود نیست.", reply_markup=back_keyboard())
    else:
        await state.set_state(ManageFiles.file_number)
        await callback.message.edit_text(
            "شماره فایل مورد نظر را ارسال کنید:\n\n"
            f"تعداد فایل‌ها: {files_count}",
            reply_markup=back_keyboard()
        )

@router.message(ManageFiles.file_number, F.text.isdigit())
async def get_file_by_number(message: types.Message, state: FSMContext):
    file_number = int(message.text)
    file_data = await db.get_file_by_number(file_number)
    if not file_data:
        await message.answer("فایلی با این شماره وجود ندارد.", reply_markup=back_keyboard())
        return

    file_message = await get_file_message(message.bot, file_data)
    await message.answer(**file_message, reply_markup=get_files_keyboard(file_number))
    await state.clear()

@router.callback_query(F.data.startswith("delete_file:"))
async def delete_file_callback(callback: types.CallbackQuery):
    file_id = int(callback.data.split(":")[1])
    await delete_file(callback.bot, file_id)
    await callback.message.edit_text("فایل با موفقیت حذف شد.", reply_markup=back_keyboard())
