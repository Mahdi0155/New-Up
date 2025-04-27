from aiogram.fsm.state import State, StatesGroup

class CreatePost(StatesGroup):
    waiting_for_file = State()
    waiting_for_caption = State()
    confirm_send_to_channel = State()
