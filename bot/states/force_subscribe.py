from aiogram.fsm.state import State, StatesGroup

class ForceSubscribe(StatesGroup):
    waiting_for_channel_username = State()
    waiting_for_remove_channel_username = State()
