# handlers/force_subscription/force_subscription_handler.py

from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db, bot
from keyboards.inline.force_channels_keyboard import force_channels_keyboard
from states.admin_states import ForceSubscriptionState

@dp.message_handler(text="🔗 عضویت اجباری", is_admin=True)
async def manage_force_channels(message: types.Message):
    channels = db.get_all_force_channels()
    if not channels:
        text = "هیچ کانالی ثبت نشده. برای افزودن کانال، روی گزینه زیر کلیک کن."
    else:
        text = "لیست کانال‌های اجباری:\n\n"
        for idx, ch in enumerate(channels, 1):
            text += f"{idx}. {ch['title']} ({ch['username']})\n"
    await message.answer(text, reply_markup=force_channels_keyboard())

@dp.callback_query_handler(text="add_force_channel", is_admin=True)
async def add_force_channel(call: types.CallbackQuery):
    await call.message.edit_text("لطفا یوزرنیم کانال رو بفرست (مثلا: @mychannel)")
    await ForceSubscriptionState.waiting_for_channel_username.set()

@dp.message_handler(state=ForceSubscriptionState.waiting_for_channel_username, is_admin=True)
async def save_force_channel(message: types.Message, state: FSMContext):
    username = message.text.strip()
    try:
        chat = await bot.get_chat(username)
        db.add_force_channel(chat.id, chat.title, username)
        await message.answer(f"کانال {chat.title} با موفقیت اضافه شد.", reply_markup=force_channels_keyboard())
    except Exception as e:
        await message.answer("مشکلی پیش اومد! مطمئن شو که بات توی اون کانال ادمینه.")
    await state.finish()

@dp.callback_query_handler(lambda c: c.data.startswith("remove_force_channel_"), is_admin=True)
async def remove_force_channel(call: types.CallbackQuery):
    channel_id = int(call.data.split("_")[-1])
    db.remove_force_channel(channel_id)
    await call.message.edit_text("کانال با موفقیت حذف شد.", reply_markup=force_channels_keyboard())
