from aiogram import types
from aiogram.fsm.context import FSMContext
from src.loader import dp, bot
from src.keyboards import main_keyboard
from src.database import get_file

@dp.message(commands=["start"])
async def start_handler(message: types.Message, state: FSMContext):
    args = message.text.split()

    if len(args) > 1 and args[1].startswith("file_"):
        # حالت استارت با فایل
        file_id = args[1].replace("file_", "")
        file_data = await get_file(file_id)

        if not file_data:
            await message.answer("❌ فایل مورد نظر پیدا نشد.")
            return

        await bot.send_video(
            chat_id=message.chat.id,
            video=file_data["file_id"],
            caption=file_data["caption"]
        )

    else:
        # حالت معمولی
        await message.answer("سلام خوش اومدی!", reply_markup=main_keyboard())
