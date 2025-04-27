from aiogram.fsm.state import State, StatesGroup

class AddForcedChannel(StatesGroup):
    waiting_for_channel_username = State()
