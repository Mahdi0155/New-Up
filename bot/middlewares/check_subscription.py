from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from loader import bot
from utils.db import Database
from data.config import CHANNELS

db = Database()

class CheckSubscriptionMiddleware(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user_id = update.message.from_user.id
        elif update.callback_query:
            user_id = update.callback_query.from_user.id
        else:
            return

        for channel in CHANNELS:
            try:
                member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            except Exception:
                member = None

            if member is None or member.status not in ['creator', 'administrator', 'member']:
                data['is_subscribed'] = False
                return

        data['is_subscribed'] = True
