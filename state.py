from aiogram.dispatcher.filters.state import StatesGroup, State

class Users_text(StatesGroup):
    user_translate_text_en_ru = State()
    user_translate_text_ru_en = State()
    user_translate_text_en_uz = State()
    user_translate_text_uz_en = State()
    user_translate_photo_en_ru = State()
    user_translate_photo_ru_en = State()
    user_translate_photo_en_uz = State()
    user_translate_photo_uz_en = State()



class Names_media(StatesGroup):
    media_name = State()
    voice_name = State()
    bbook_name = State()
    social_insta_link = State()
    social_yout_link = State()



