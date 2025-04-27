from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit=0.5):
        self.rate_limit = limit
        self._user_last_call = {}
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: Message, data: dict):
        handler = current_handler()
        if handler is None:
            return

        user_id = message.from_user.id
        current_time = message.date.timestamp()

        if user_id in self._user_last_call:
            delta = current_time - self._user_last_call[user_id]
            if delta < self.rate_limit:
                raise CancelHandler()

        self._user_last_call[user_id] = current_time
