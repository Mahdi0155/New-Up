from aiogram import types
from aiogram.fsm.context import FSMContext
from src.loader import dp
from src.states import UploadState

@dp.message(UploadState.waiting_for_new_caption)
async def new_caption_handler(message: types.Message, state: FSMContext):
    new_caption = message.text

    # ذخیره کپشن جدید در state
    await state.update_data(caption=new_caption)

    # ارسال پیام تایید به ادمین
    await message.answer(
        f"✅ کپشن جدید ذخیره شد:\n\n{new_caption}\n\n"
        "حالا دکمه تایید نهایی رو بزن که فایل به کانال ارسال بشه."
    )

    # تغییر وضعیت به حالت تایید نهایی
    await state.set_state(UploadState.confirm_upload)
