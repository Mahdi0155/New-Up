# src/main.py

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from config import TOKEN
from handlers import admin_handlers, user_handlers, common_handlers
from middlewares.membership_checker import MembershipChecker

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot)

# Middleware عضویت
dp.middleware.setup(MembershipChecker())

# ثبت هندلرها
admin_handlers.register_admin_handlers(dp)
user_handlers.register_user_handlers(dp)
common_handlers.register_common_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
