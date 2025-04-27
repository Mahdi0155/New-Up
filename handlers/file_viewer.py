from aiogram import types
from loader import dp, db, bot
from utils.check_subscription import check_user_subscriptions

CHANNELS = ["@channel1", "@channel2"]

@dp.message_handler(lambda message: message.text and message.text.startswith("/start view_"))
async def view_file(message: types.Message):
    user_id = message.from_user.id

    # بررسی عضویت
    result = await check_user_subscriptions(user_id, CHANNELS)
    if not result:
        markup = types.InlineKeyboardMarkup(row_width=1)
        for ch in CHANNELS:
            markup.add(types.InlineKeyboardButton("عضویت در کانال", url=f"https://t.me/{ch[1:]}"))
        markup.add(types.InlineKeyboardButton("✅ عضویت انجام شد", callback_data="check_subs_view"))
        await message.answer("لطفا ابتدا در کانال های زیر عضو شوید:", reply_markup=markup)
        return

    file_short_id = message.text.split("_")[1]

    file_data = db.get_file_by_short_id(file_short_id)
    if not file_data:
        await message.answer("❌ فایل مورد نظر پیدا نشد یا حذف شده است.")
        return

    file_id = file_data['file_id']
    caption = file_data['caption']
    file_type = file_data['file_type']

    try:
        if file_type == "photo":
            sent = await message.answer_photo(photo=file_id, caption=caption)
        elif file_type == "video":
            sent = await message.answer_video(video=file_id, caption=caption)
        else:
            await message.answer("❌ فرمت فایل پشتیبانی نمی‌شود.")
            return

        await message.answer("⏳ این فایل تا ۱۵ ثانیه دیگر حذف خواهد شد. لطفاً ذخیره کنید.")

        # حذف فایل بعد از ۱۵ ثانیه
        await bot.delete_message(chat_id=message.chat.id, message_id=sent.message_id, delay=15)

    except Exception as e:
        await message.answer(f"خطایی رخ داد: {e}")

# چک عضویت بعد از ورود به مشاهده فایل
@dp.callback_query_handler(text="check_subs_view")
async def recheck_subscription_view(call: types.CallbackQuery):
    user_id = call.from_user.id

    result = await check_user_subscriptions(user_id, CHANNELS)
    if result:
        await call.message.edit_text("✅ عضویت تایید شد. حالا دوباره روی لینک مشاهده فایل کلیک کنید.")
    else:
        await call.answer("هنوز عضو نشدید.", show_alert=True)
