from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.check_sub import check_sub_channel


class CheckSubChannelMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        if message.chat.type != 'private':
            return

        is_subscribed = await check_sub_channel(message.from_user.id)
        if not is_subscribed:
            await message.answer("لطفا ابتدا در کانال عضو شوید سپس دوباره تلاش کنید.")
            raise Exception("User not subscribed.")
