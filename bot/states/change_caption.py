from aiogram.fsm.state import State, StatesGroup

class ChangeCaption(StatesGroup):
    waiting_for_new_caption = State()
