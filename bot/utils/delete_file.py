from loader import db
from aiogram import types

async def delete_file_by_id(file_id: int, bot: types.Bot):
    file = await db.get_file_by_id(file_id)
    if not file:
        return False

    try:
        await bot.delete_message(chat_id=file['chat_id'], message_id=file['message_id'])
    except Exception as e:
        print(f"Error deleting message: {e}")

    await db.delete_file(file_id)
    return True
