import asyncio
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from typing import Callable


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: float = DEFAULT_RATE_LIMIT, key_prefix: str = 'antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        handler = data.get('handler')
        dispatcher = self.dispatcher

        if handler:
            limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"

        try:
            await dispatcher.throttle(key, rate=limit)
        except asyncio.exceptions.CancelledError:
            raise
        except Exception:
            await message.reply("لطفا کمی آهسته‌تر!")
            raise
