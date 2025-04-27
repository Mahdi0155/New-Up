# bot/handlers/admin.py

from aiogram import types, Router, F
from aiogram.filters import Command
from bot.keyboards.admin_keyboards import admin_panel_keyboard, back_to_menu_keyboard
from bot.utils.database import get_admins, add_admin, remove_admin
from config import SUPER_ADMIN_ID

router = Router()

# نمایش پنل مدیریت ادمین‌ها
@router.message(Command("manage_admins"))
async def manage_admins(message: types.Message):
    if message.from_user.id != SUPER_ADMIN_ID:
        return await message.answer("❌ شما دسترسی به این بخش ندارید.")

    admins = await get_admins()
    admins_list = "\n".join(f"- `{admin_id}`" for admin_id in admins) or "ادمینی وجود ندارد."
    text = f"🛡️ لیست ادمین‌های فعلی:\n\n{admins_list}\n\n➕ برای اضافه کردن ادمین، آی‌دی عددی را ارسال کنید.\n➖ برای حذف، قبل از آی‌دی عددی علامت `-` بگذارید.\n\n🔙 یا گزینه بازگشت را بزنید."
    await message.answer(text, reply_markup=back_to_menu_keyboard())

# دریافت آی‌دی ادمین برای اضافه یا حذف
@router.message(F.text.regexp(r"^-?\d+$"))
async def handle_admin_update(message: types.Message):
    if message.from_user.id != SUPER_ADMIN_ID:
        return await message.answer("❌ شما دسترسی به این بخش ندارید.")

    admin_id = int(message.text)

    if admin_id > 0:
        # افزودن ادمین
        success = await add_admin(admin_id)
        if success:
            await message.answer(f"✅ ادمین جدید با آی‌دی `{admin_id}` اضافه شد.", parse_mode="Markdown")
        else:
            await message.answer("⚠️ این ادمین قبلاً ثبت شده بود.")
    else:
        # حذف ادمین
        admin_id = abs(admin_id)
        success = await remove_admin(admin_id)
        if success:
            await message.answer(f"✅ ادمین با آی‌دی `{admin_id}` حذف شد.", parse_mode="Markdown")
        else:
            await message.answer("⚠️ چنین ادمینی وجود ندارد.")

    await manage_admins(message)

# بازگشت به منوی اصلی
@router.message(F.text == "🔙 بازگشت به منو")
async def back_to_menu(message: types.Message):
    from bot.handlers.start import start  # ایمپورت در لحظه برای جلوگیری از چرخش ایمپورت
    await start(message)
