from aiogram.fsm.state import StatesGroup, State

class FileManagement(StatesGroup):
    select_file = State()
    confirm_delete = State()
