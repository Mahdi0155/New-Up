from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot
from keyboards.admin import admin_panel
from utils.check_admin import is_admin

# --- وضعیت های کپشن و تایید ---
class UploadStates(StatesGroup):
    waiting_for_caption = State()
    waiting_for_confirm = State()

# --- هندلر دریافت فایل از ادمین ---
@dp.message(lambda message: message.content_type in ['photo', 'video'])
async def handle_file(message: types.Message, state: FSMContext):
    if not await is_admin(message.from_user.id):
        return

    file_id = message.photo[-1].file_id if message.content_type == 'photo' else message.video.file_id
    file_type = message.content_type

    await state.update_data(file_id=file_id, file_type=file_type)
    await message.answer("لطفاً کپشن مورد نظر برای فایل رو وارد کن:")
    await state.set_state(UploadStates.waiting_for_caption)

# --- هندلر دریافت کپشن ---
@dp.message(UploadStates.waiting_for_caption)
async def handle_caption(message: types.Message, state: FSMContext):
    caption = message.text
    await state.update_data(caption=caption)

    data = await state.get_data()

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ تایید و ارسال", callback_data="confirm_send"),
            InlineKeyboardButton(text="✏️ ویرایش کپشن", callback_data="edit_caption")
        ]
    ])

    if data['file_type'] == 'photo':
        await bot.send_photo(chat_id=message.chat.id, photo=data['file_id'], caption=caption, reply_markup=keyboard)
    elif data['file_type'] == 'video':
        await bot.send_video(chat_id=message.chat.id, video=data['file_id'], caption=caption, reply_markup=keyboard)

    await state.set_state(UploadStates.waiting_for_confirm)
