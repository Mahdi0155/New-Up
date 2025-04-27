from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from bot.keyboards import manage_files_kb
from bot.database.models import File
from bot.states.admin import ManageFilesState
from bot.filters import AdminFilter

router = Router()
router.message.filter(AdminFilter())

@router.message(Command("manage_files"))
async def cmd_manage_files(message: types.Message, state: FSMContext):
    await state.set_state(ManageFilesState.waiting_for_file_id)
    await message.answer("لطفا آی‌دی فایل را برای مدیریت ارسال کنید.", reply_markup=manage_files_kb.back_to_menu_kb())

@router.message(ManageFilesState.waiting_for_file_id, F.text)
async def process_file_id(message: types.Message, state: FSMContext):
    file_id = message.text
    file = await File.get_or_none(id=file_id)

    if not file:
        await message.answer("فایلی با این آی‌دی پیدا نشد. لطفا دوباره تلاش کنید.", reply_markup=manage_files_kb.back_to_menu_kb())
        return

    text = f"کپشن فایل:\n\n{file.caption or 'کپشنی موجود نیست.'}"
    await message.answer(text, reply_markup=manage_files_kb.file_manage_kb(file.id))
    await state.clear()
