from aiogram.fsm.state import State, StatesGroup

class ManageForcedSubscription(StatesGroup):
    waiting_for_add_channel = State()
    waiting_for_remove_channel = State()
