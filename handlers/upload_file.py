from aiogram import Router, F
from aiogram.types import Message, InputFile, FSInputFile
from states import UploadFileState
from aiogram.fsm.context import FSMContext
from config import ADMINS
from database import save_file
from keyboards import confirm_keyboard
import os
from utils import get_file_link

router = Router()

@router.message(F.text == "آپلود فایل جدید")
async def upload_file_handler(message: Message, state: FSMContext):
    if str(message.from_user.id) not in ADMINS:
        return
    await message.answer("لطفاً فایل مورد نظر (عکس یا ویدیو) را ارسال کنید:")
    await state.set_state(UploadFileState.waiting_for_file)

@router.message(UploadFileState.waiting_for_file, F.content_type.in_({"photo", "video"}))
async def receive_file_handler(message: Message, state: FSMContext):
    file_id = message.photo[-1].file_id if message.photo else message.video.file_id
    await state.update_data(file_id=file_id)
    await message.answer("لطفاً کپشن فایل را وارد کنید:")
    await state.set_state(UploadFileState.waiting_for_caption)

@router.message(UploadFileState.waiting_for_caption)
async def receive_caption_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    file_id = data["file_id"]
    caption = message.text

    # ذخیره فایل موقت
    file_unique_id = message.photo[-1].file_unique_id if message.photo else message.video.file_unique_id
    file_name = f"{file_unique_id}.txt"
    save_file(file_id, caption, file_name)

    # آماده سازی پیش‌نمایش
    file_link = get_file_link(file_name)
    preview_text = f"{caption}\n\n[مشاهده فایل]({file_link})"
    await message.answer(
        "پیش‌نمایش پیام آماده شد. تایید کنید یا ویرایش کنید.",
        reply_markup=confirm_keyboard()
    )
    await state.clear()
