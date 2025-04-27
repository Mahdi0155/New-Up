from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

from bot.loader import dp
from bot.states import UploadFile
from bot.keyboards import confirm_send_to_channel


@dp.message_handler(content_types=[ContentType.PHOTO, ContentType.VIDEO], state="*")
async def upload_file_handler(message: types.Message, state: FSMContext):
    await message.answer("لطفا کپشن فایل را وارد کنید:")
    await state.update_data(file=message)
    await UploadFile.caption.set()


@dp.message_handler(state=UploadFile.caption)
async def get_caption_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    file_message = data.get("file")
    caption = message.text

    await state.update_data(caption=caption)

    await message.answer(
        "آیا مایلید این فایل را به کانال ارسال کنید؟",
        reply_markup=confirm_send_to_channel.get_confirm_keyboard()
    )
