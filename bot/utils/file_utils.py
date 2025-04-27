from aiogram.types import Message


async def get_file_id(message: Message) -> str:
    if message.photo:
        return message.photo[-1].file_id
    elif message.video:
        return message.video.file_id
    else:
        return None
