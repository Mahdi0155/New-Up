from aiogram.fsm.state import State, StatesGroup

class ManageAdmins(StatesGroup):
    waiting_for_add_admin_id = State()
    waiting_for_remove_admin_id = State()
