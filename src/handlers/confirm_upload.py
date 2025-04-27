from aiogram import types
from aiogram.fsm.context import FSMContext
from src.loader import dp, bot, CHANNEL_ID
from src.states import UploadState
from src.database import save_file

@dp.message(UploadState.confirm_upload)
async def confirm_upload_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    file_id = data.get("file_id")
    caption = data.get("caption", "")

    # ارسال فایل به کانال
    sent_message = await bot.send_video(
        chat_id=CHANNEL_ID,
        video=file_id,
        caption=f"{caption}\n\n🔵 [مشاهده فایل](https://t.me/{(await bot.get_me()).username}?start=file_{sent_message.message_id})",
        parse_mode="Markdown"
    )

    # ذخیره فایل در دیتابیس
    await save_file(sent_message.message_id, file_id, caption)

    await message.answer("✅ فایل با موفقیت به کانال ارسال شد.")

    await state.clear()
