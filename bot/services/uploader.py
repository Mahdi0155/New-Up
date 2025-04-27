from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot
from utils.db import add_file, get_file
from data.config import ADMINS, UPLOAD_CHANNEL
import asyncio

async def upload_file(message: types.Message):
    if not message.photo and not message.video:
        await message.answer("فقط عکس یا فیلم قابل آپلود است.")
        return

    await message.answer("لطفاً کپشن فایل را وارد کنید:")

    @dp.message_handler(lambda m: m.reply_to_message and m.reply_to_message.text == "لطفاً کپشن فایل را وارد کنید:")
    async def get_caption(msg: types.Message):
        file_id = None
        if message.photo:
            file_id = message.photo[-1].file_id
        elif message.video:
            file_id = message.video.file_id

        caption = msg.text
        data = await add_file(file_id, caption)

        view_link = f"https://t.me/{bot.username}?start=file_{data['file_unique_id']}"

        send_caption = f"{caption}\n\n[مشاهده فایل]({view_link})"

        confirm_markup = InlineKeyboardMarkup()
        confirm_markup.add(InlineKeyboardButton("✅ تایید و ارسال به کانال", callback_data=f"confirm_send:{data['file_unique_id']}"))
        confirm_markup.add(InlineKeyboardButton("✏️ ویرایش کپشن", callback_data=f"edit_caption:{data['file_unique_id']}"))

        await msg.answer(send_caption, parse_mode="Markdown", reply_markup=confirm_markup)

async def send_file_to_user(user_id, file_unique_id):
    file = await get_file(file_unique_id)
    if not file:
        await bot.send_message(user_id, "فایل یافت نشد یا حذف شده است.")
        return

    await bot.send_message(user_id, "توجه: این فایل فقط ۱۵ ثانیه قابل مشاهده است. لطفاً سریع ذخیره کنید.")

    if file['file_type'] == 'photo':
        sent = await bot.send_photo(user_id, file['file_id'], caption=file['caption'])
    else:
        sent = await bot.send_video(user_id, file['file_id'], caption=file['caption'])

    await asyncio.sleep(15)
    try:
        await sent.delete()
    except:
        pass
