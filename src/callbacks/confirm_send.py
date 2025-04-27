from aiogram import types
from aiogram.fsm.context import FSMContext

from src.loader import bot, dp
from src.data.config import CHANNEL_ID

@dp.callback_query(lambda c: c.data.startswith("confirm_send"))
async def confirm_send_to_channel(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()

    data = callback_query.data.split(":")
    file_id = data[1]
    caption_text = data[2]

    # فرستادن فایل با کپشن به کانال
    try:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=caption_text,
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
        await callback_query.message.answer("✅ پیام با موفقیت به کانال ارسال شد!")
    except Exception as e:
        await callback_query.message.answer(f"❌ ارسال پیام به کانال با خطا مواجه شد: {e}")

    await state.clear()
