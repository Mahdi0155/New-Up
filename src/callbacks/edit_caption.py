from aiogram import types
from aiogram.fsm.context import FSMContext
from src.loader import dp
from src.states import UploadState

@dp.callback_query(lambda c: c.data.startswith("edit_caption"))
async def edit_caption(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()

    # تغییر وضعیت FSM به انتظار کپشن جدید
    await state.set_state(UploadState.waiting_for_new_caption)

    await callback_query.message.answer("✏️ لطفا کپشن جدید را وارد کنید:")
