from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.keyboards.admin.subscription import subscription_keyboard
from bot.loader import dp, db
from bot.states.admin import SubscriptionStates

@dp.message_handler(text="➕ مدیریت عضویت اجباری", state="*")
async def manage_subscription(message: types.Message):
    await message.answer("لطفا یکی از گزینه‌های زیر را انتخاب کنید:", reply_markup=subscription_keyboard())
    await SubscriptionStates.main.set()

@dp.message_handler(state=SubscriptionStates.main)
async def handle_subscription_option(message: types.Message, state: FSMContext):
    if message.text == "➕ اضافه کردن کانال":
        await message.answer("لطفا آیدی کانال را ارسال کنید:")
        await SubscriptionStates.add_channel.set()

    elif message.text == "➖ حذف کردن کانال":
        await message.answer("لطفا آیدی کانالی که میخواهید حذف کنید را ارسال کنید:")
        await SubscriptionStates.remove_channel.set()

    elif message.text == "🔙 بازگشت":
        await message.answer("به منوی مدیریت بازگشتید.", reply_markup=subscription_keyboard())
        await state.finish()

@dp.message_handler(state=SubscriptionStates.add_channel)
async def add_channel(message: types.Message, state: FSMContext):
    channel_id = message.text.strip()
    await db.add_channel(channel_id)
    await message.answer(f"کانال {channel_id} اضافه شد.", reply_markup=subscription_keyboard())
    await SubscriptionStates.main.set()

@dp.message_handler(state=SubscriptionStates.remove_channel)
async def remove_channel(message: types.Message, state: FSMContext):
    channel_id = message.text.strip()
    await db.remove_channel(channel_id)
    await message.answer(f"کانال {channel_id} حذف شد.", reply_markup=subscription_keyboard())
    await SubscriptionStates.main.set()
