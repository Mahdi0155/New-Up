# config.py

import os

TOKEN = os.getenv('BOT_TOKEN')  # توی هاستت باید توی Environment Variables ست کنی
ADMINS = [123456789]  # آی‌دی عددی ادمین‌های اصلی اینجا
CHANNELS = ['@YourChannel1', '@YourChannel2']  # کانال‌هایی که عضویت اجباری باید بشن
DATABASE_URL = os.getenv('DATABASE_URL')  # لینک دیتابیس اگر نیاز باشه
MAX_FILE_SIZE_MB = 200  # حداکثر حجم فایل مجاز آپلود
DELETE_AFTER_SECONDS = 15  # چند ثانیه بعد ارسال، فایل حذف بشه
