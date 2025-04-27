from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from config import config

async def send_to_channel(bot: Bot, text: str, reply_markup=None):
    try:
        message = await bot.send_message(
            chat_id=config.CHANNEL_ID,
            text=text,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
        return message.message_id
    except TelegramBadRequest as e:
        print(f"Failed to send message to channel: {e}")
        return None
