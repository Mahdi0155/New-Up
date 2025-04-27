from aiogram.fsm.state import State, StatesGroup

class ChangeForcedSubscription(StatesGroup):
    waiting_for_channel_id = State()
