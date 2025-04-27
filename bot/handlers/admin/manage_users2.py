from aiogram import Router, types
from aiogram.filters import Command
from bot.keyboards import manage_users_kb
from database import users_db

router = Router()

@router.message(Command("manage_users"))
async def manage_users(message: types.Message):
    await message.answer("لطفاً یک گزینه انتخاب کنید:", reply_markup=manage_users_kb.get_keyboard())

@router.callback_query(lambda c: c.data.startswith("user_action:"))
async def user_action_callback(callback_query: types.CallbackQuery):
    action = callback_query.data.split(":")[1]
    
    if action == "list":
        users = await users_db.get_all_users()
        text = "لیست کاربران ثبت شده:\n"
        for user in users:
            text += f"- {user['user_id']}\n"
        await callback_query.message.answer(text)
    
    elif action == "count":
        count = await users_db.get_users_count()
        await callback_query.message.answer(f"تعداد کل کاربران: {count}")
    
    await callback_query.answer()
