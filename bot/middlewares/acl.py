from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

class ACLMiddleware(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        # اینجا میتونی هر جور محدودیتی بخوای بزاری
        pass
