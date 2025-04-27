from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import CHANNELS
from utils.check_subscription import check_subscription


class CheckSubscriptionMiddleware(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user_id = update.message.from_user.id
        elif update.callback_query:
            user_id = update.callback_query.from_user.id
        else:
            return

        for channel in CHANNELS:
            is_member = await check_subscription(user_id=user_id, channel=channel)
            if not is_member:
                link = await update.bot.export_chat_invite_link(channel)
                await update.bot.send_message(
                    chat_id=user_id,
                    text=f"برای استفاده از ربات، ابتدا در کانال عضو شوید:\n{link}"
                )
                raise Exception("User is not subscribed")
