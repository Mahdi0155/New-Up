from aiogram.fsm.state import State, StatesGroup

class AddAdmin(StatesGroup):
    waiting_for_admin_id = State()
