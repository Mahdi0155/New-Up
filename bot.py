# bot.py

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from config import TOKEN, ADMINS, CHANNELS, DELETE_AFTER_SECONDS

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO)

# ساخت بات و دیسپچر
bot = Bot(token=TOKEN)
dp = Dispatcher()

# کیبورد عضویت اجباری
def join_keyboard():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="عضویت در کانال", url="https://t.me/" + CHANNELS[0][1:])],
        [InlineKeyboardButton(text="بررسی عضویت", callback_data="check_join")]
    ])
    return markup

# چک کردن عضویت کاربر
async def is_subscribed(user_id):
    for channel in CHANNELS:
        try:
            member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status not in ('member', 'creator', 'administrator'):
                return False
        except Exception:
            return False
    return True

# شروع ربات
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    if not await is_subscribed(message.from_user.id):
        await message.answer(
            "لطفا ابتدا در کانال عضو شوید.",
            reply_markup=join_keyboard()
        )
        return
    await message.answer("سلام! فایل خود را ارسال کنید.")

# هندل فایل‌های دریافتی (عکس یا ویدیو)
@dp.message(lambda message: message.photo or message.video)
async def file_handler(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("شما اجازه آپلود ندارید.")
        return

    file_id = message.photo[-1].file_id if message.photo else message.video.file_id
    file_type = "photo" if message.photo else "video"

    await message.answer("لطفاً کپشن مورد نظر خود را ارسال کنید:")

    # ذخیره موقت
    state = dp.fsm.create_key(message.from_user.id)
    await state.set_data({"file_id": file_id, "file_type": file_type})

# گرفتن کپشن بعد از فایل
@dp.message(lambda message: True)
async def caption_handler(message: types.Message):
    state = dp.fsm.get_key(message.from_user.id)
    if not state:
        return

    data = await state.get_data()
    file_id = data["file_id"]
    file_type = data["file_type"]
    caption = message.text

    view_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="مشاهده", url="https://t.me/YourBotUsername?start=" + file_id)]
        ]
    )

    # ارسال پیش‌نمایش به ادمین
    if file_type == "photo":
        sent = await message.answer_photo(photo=file_id, caption=f"{caption}\n\n⬇️ مشاهده فایل ⬇️", reply_markup=view_button)
    else:
        sent = await message.answer_video(video=file_id, caption=f"{caption}\n\n⬇️ مشاهده فایل ⬇️", reply_markup=view_button)

    await state.clear()

    # تایید نهایی
    confirm_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="تایید ارسال به کانال", callback_data=f"confirm_send:{file_id}:{file_type}:{sent.message_id}")]
        ]
    )
    await message.answer("آیا مایلید این فایل به کانال ارسال شود؟", reply_markup=confirm_markup)

# تایید ارسال به کانال
@dp.callback_query(lambda call: call.data.startswith("confirm_send"))
async def confirm_send_handler(call: types.CallbackQuery):
    parts = call.data.split(":")
    file_id = parts[1]
    file_type = parts[2]
    preview_message_id = int(parts[3])

    caption_message = await bot.forward_message(chat_id=call.from_user.id, from_chat_id=call.from_user.id, message_id=preview_message_id)

    if file_type == "photo":
        await bot.send_photo(chat_id=CHANNELS[0], photo=file_id, caption=caption_message.caption)
    else:
        await bot.send_video(chat_id=CHANNELS[0], video=file_id, caption=caption_message.caption)

    await call.answer("فایل به کانال ارسال شد.")

# بررسی عضویت
@dp.callback_query(lambda call: call.data == "check_join")
async def check_join_handler(call: types.CallbackQuery):
    if await is_subscribed(call.from_user.id):
        await call.message.delete()
        await call.message.answer("عضویت تایید شد! حالا فایل خود را ارسال کنید.")
    else:
        await call.answer("لطفاً ابتدا عضو شوید.", show_alert=True)

# اجرای ربات
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
