from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from src.loader import bot, dp
from src.keyboards.reply import back_button
from src.states.upload_state import UploadFile
from src.data.config import CHANNEL_ID

@dp.message(UploadFile.waiting_for_caption)
async def save_caption(message: types.Message, state: FSMContext):
    data = await state.get_data()
    file_id = data.get("file_id")

    # ساختن متن پیام نهایی
    caption_text = message.text + "\n\n[مشاهده](https://t.me/your_bot_username?start=file_" + file_id + ")"

    # ساخت دکمه‌های تایید و ویرایش
    buttons = [
        [InlineKeyboardButton(text="✅ تایید ارسال", callback_data=f"confirm_send:{file_id}:{caption_text}")],
        [InlineKeyboardButton(text="✏️ ویرایش کپشن", callback_data="edit_caption")],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)

    await message.answer(
        f"پیش نمایش پیام ارسالی:\n\n{caption_text}",
        reply_markup=markup,
        disable_web_page_preview=True
    )

    await state.update_data(caption=message.text)
    await state.set_state(UploadFile.confirmation)
