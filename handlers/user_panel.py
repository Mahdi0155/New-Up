from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import dp, db, bot
from states.admin_states import AdminPanel
from keyboards.inline.admin_keyboards import admin_main_keyboard, manage_files_keyboard
from utils.file_manager import delete_file_by_id

ADMIN_IDS = [123456789]  # اینجا آیدی خودت و آیدی‌های ادمین‌های دیگه رو لیست کن

# هندلر ورود به پنل ادمین
@dp.message_handler(commands=['admin'], user_id=ADMIN_IDS)
async def enter_admin_panel(message: types.Message):
    await message.answer("به پنل مدیریت خوش آمدید:", reply_markup=admin_main_keyboard())

# مدیریت فایل ها
@dp.callback_query_handler(text="manage_files", user_id=ADMIN_IDS)
async def manage_files(call: types.CallbackQuery):
    files = db.get_all_files()
    if not files:
        await call.message.edit_text("هیچ فایلی پیدا نشد.", reply_markup=admin_main_keyboard())
        return

    await call.message.edit_text(f"تعداد کل فایل‌ها: {len(files)}\n\nلطفا عدد فایل مورد نظر برای مدیریت را ارسال کنید:", reply_markup=manage_files_keyboard())
    await AdminPanel.waiting_for_file_id.set()

# دریافت آیدی فایل برای مدیریت
@dp.message_handler(state=AdminPanel.waiting_for_file_id, user_id=ADMIN_IDS)
async def select_file_to_manage(message: types.Message, state: FSMContext):
    file_number = message.text.strip()

    if not file_number.isdigit():
        await message.answer("لطفا فقط عدد ارسال کنید.")
        return

    file_id = int(file_number)
    file_info = db.get_file_by_number(file_id)

    if not file_info:
        await message.answer("فایلی با این شماره وجود ندارد.")
        return

    # ذخیره آی‌دی فایل در وضعیت
    await state.update_data(selected_file_id=file_id)

    # ارسال فایل و کپشن
    try:
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=file_info['file_id'],
            caption=f"{file_info['caption']}\n\n[مشاهده فایل]({file_info['link']})",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("❌ حذف فایل", callback_data="delete_file"))
        )
    except:
        try:
            await bot.send_video(
                chat_id=message.chat.id,
                video=file_info['file_id'],
                caption=f"{file_info['caption']}\n\n[مشاهده فایل]({file_info['link']})",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton("❌ حذف فایل", callback_data="delete_file"))
            )
        except Exception as e:
            await message.answer(f"خطا در ارسال فایل: {e}")

# حذف فایل
@dp.callback_query_handler(text="delete_file", state=AdminPanel.waiting_for_file_id, user_id=ADMIN_IDS)
async def delete_selected_file(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    file_id = data.get("selected_file_id")

    if not file_id:
        await call.answer("مشکلی پیش آمد. لطفا دوباره امتحان کنید.", show_alert=True)
        return

    success = delete_file_by_id(file_id)

    if success:
        await call.message.edit_text("✅ فایل با موفقیت حذف شد.", reply_markup=admin_main_keyboard())
    else:
        await call.message.edit_text("⚠️ مشکلی در حذف فایل پیش آمد.", reply_markup=admin_main_keyboard())

    await state.finish()

# برگشت به پنل
@dp.callback_query_handler(text="back_to_admin", user_id=ADMIN_IDS, state="*")
async def back_to_admin(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("به پنل مدیریت برگشتید.", reply_markup=admin_main_keyboard())
    await state.finish()
