from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, db
from states.channel_states import ManageChannels
from keyboards.default import admin_panel

@dp.message_handler(text="مدیریت عضویت اجباری", is_admin=True)
async def manage_channels(message: types.Message):
    channels = await db.get_all_channels()
    
    if not channels:
        await message.answer("در حال حاضر کانالی اضافه نشده است.", reply_markup=admin_panel.back_button())
    else:
        text = "لیست کانال‌های فعلی:\n\n"
        for channel in channels:
            text += f"- {channel['title']} ({channel['channel_id']})\n"
        await message.answer(text, reply_markup=admin_panel.channels_buttons())

    await ManageChannels.Choosing.set()

@dp.message_handler(state=ManageChannels.Choosing, text="➕ افزودن کانال")
async def add_channel(message: types.Message, state: FSMContext):
    await message.answer("لطفاً آیدی یا آدرس کانال را ارسال کنید:")
    await ManageChannels.Adding.set()

@dp.message_handler(state=ManageChannels.Adding)
async def save_channel(message: types.Message, state: FSMContext):
    channel_id = message.text.strip()
    await db.add_channel(channel_id)
    await message.answer("✅ کانال اضافه شد.", reply_markup=admin_panel.back_button())
    await state.finish()

@dp.message_handler(state=ManageChannels.Choosing, text="➖ حذف کانال")
async def delete_channel_prompt(message: types.Message, state: FSMContext):
    await message.answer("آیدی یا آدرس کانال موردنظر برای حذف را ارسال کنید:")
    await ManageChannels.Deleting.set()

@dp.message_handler(state=ManageChannels.Deleting)
async def delete_channel(message: types.Message, state: FSMContext):
    channel_id = message.text.strip()
    await db.delete_channel(channel_id)
    await message.answer("✅ کانال حذف شد.", reply_markup=admin_panel.back_button())
    await state.finish()
