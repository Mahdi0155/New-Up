from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.loader import dp, db
from bot.keyboards import manage_forced_channels_keyboard, back_keyboard
from bot.states import ManageForcedChannelsState


@dp.message_handler(Text(equals="👤 عضویت اجباری"), state="*")
async def manage_forced_channels(message: types.Message, state: FSMContext):
    await state.finish()
    channels = await db.get_forced_channels()
    keyboard = await manage_forced_channels_keyboard(channels)
    await message.answer("مدیریت عضویت‌های اجباری:", reply_markup=keyboard)
    await ManageForcedChannelsState.waiting_for_channel_action.set()


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('delete_channel:'), state=ManageForcedChannelsState.waiting_for_channel_action)
async def delete_channel(callback_query: types.CallbackQuery, state: FSMContext):
    channel_id = int(callback_query.data.split(':')[1])
    await db.delete_forced_channel(channel_id)
    await callback_query.answer("کانال حذف شد.")
    await manage_forced_channels(callback_query.message, state)


@dp.callback_query_handler(lambda c: c.data == 'add_channel', state=ManageForcedChannelsState.waiting_for_channel_action)
async def ask_for_channel_id(callback_query: types.CallbackQuery):
    await callback_query.message.answer("آیدی عددی کانال جدید را ارسال کنید:", reply_markup=back_keyboard)
    await ManageForcedChannelsState.waiting_for_channel_id.set()


@dp.message_handler(lambda message: not message.text.isdigit(), state=ManageForcedChannelsState.waiting_for_channel_id)
async def invalid_channel_id(message: types.Message):
    await message.answer("آیدی کانال باید فقط عدد باشد. لطفا دوباره ارسال کنید.")


@dp.message_handler(lambda message: message.text.isdigit(), state=ManageForcedChannelsState.waiting_for_channel_id)
async def add_channel(message: types.Message, state: FSMContext):
    channel_id = int(message.text)
    await db.add_forced_channel(channel_id)
    await message.answer("کانال جدید اضافه شد.")
    await manage_forced_channels(message, state)
