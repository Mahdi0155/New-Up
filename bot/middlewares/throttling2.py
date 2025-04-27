from aiogram import types
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: int = DEFAULT_RATE_LIMIT, key_prefix: str = 'antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        handler = current_handler.get()
        dispatcher = message.bot.dispatcher
        if handler:
            limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"

        try:
            await dispatcher.throttle(key, rate=limit)
        except Exception:
            await message.reply("لطفاً کمی آهسته تر!")
            raise CancelHandler()

    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        handler = current_handler.get()
        dispatcher = call.bot.dispatcher
        if handler:
            limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_callback"

        try:
            await dispatcher.throttle(key, rate=limit)
        except Exception:
            await call.answer("لطفاً کمی آهسته تر!", show_alert=True)
            raise CancelHandler()
