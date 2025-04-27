# src/middlewares/membership_checker.py

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from config import FORCE_SUB_CHANNELS

class MembershipChecker(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user_id = update.message.from_user.id
            for channel_id in FORCE_SUB_CHANNELS:
                try:
                    member = await update.message.bot.get_chat_member(channel_id, user_id)
                    if member.status in ("left", "kicked"):
                        await update.message.answer("برای استفاده از ربات ابتدا باید در کانال‌های زیر عضو شوید.")
                        raise Exception("عضویت اجباری رعایت نشده")
                except Exception as e:
                    raise e
