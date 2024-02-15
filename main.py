import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message, InputFile
from aiogram.types.message import ContentType
from button import *
from state import *


from googletrans import Translator
from PIL import Image, ImageEnhance
from collections import OrderedDict
import pytesseract
import io
import re
import requests
import mysql.connector


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO)

# 6876220630:AAEdPZi3uYEzESS7jLctsdDWokeIfVeJIio
bot = Bot(token='6726751754:AAGIUmpXd4ezFmYmJu1k_ETrs8SwXZ0Ijvg', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


translator = Translator()
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="914314489",
    database="mult_function_bot"
)

cursor = connection.cursor()


@dp.message_handler(commands=['start'])
async def parse1(message: types.Message):
    cursor.execute("SELECT COUNT(*) FROM tgbot_multifunction WHERE user_id = %s;", ([message.from_user.id]))
    values = cursor.fetchone()
    if values[0] < 1:
        print("of course")
        cursor.execute("INSERT INTO tgbot_multifunction (user_id) VALUES (%s);", ([message.from_user.id]))
        connection.commit() 

    poster="bot_for_b\images\welcome.jpg"
    photo_file = types.InputFile(poster)
    await bot.send_photo(message.from_user.id, photo_file, caption=f"👋Здравствуйте {message.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)
    
     


@dp.callback_query_handler()
async def callbac(call):
    if call.data == "transl":
        box_photo = "bot_for_b\\images\\translate.jpg"
        file = types.InputMedia(media=types.InputFile(box_photo), caption="Вы можете перевести двумя способами:\n\n1. Через обычный текст\n2. Через картинку")
        await bot.edit_message_media(file, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=inline_translation)

    elif call.data == "with_text":
        box_photo = "bot_for_b\\images\\translate.jpg"
        file = types.InputMedia(media=types.InputFile(box_photo), caption="В боте есть три языка <b>Английский</b>, <b>Русский</b> и <b>Узбекский</b>")
        await bot.edit_message_media(file, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=inline_translation_text)


    elif call.data == "with_img":
        box_photo = "bot_for_b\\images\\translate.jpg"
        file = types.InputMedia(media=types.InputFile(box_photo), caption="В боте есть три языка <b>Английский</b>, <b>Русский</b> и <b>Узбекский</b>")
        await bot.edit_message_media(file, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=inline_translation_img)

    elif call.data == "back_translation":  
        box_photo = "bot_for_b\\images\\translate.jpg"
        file = types.InputMedia(media=types.InputFile(box_photo), caption="Вы можете перевести двумя способами:\n\n1. Через обычный текст\n2. Через картинку")
        await bot.edit_message_media(file, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=inline_translation)

    elif call.data == "back":
        box_photo = "bot_for_b\images\welcome.jpg"
        file = types.InputMedia(media=types.InputFile(box_photo), caption=f"👋Здравствуйте {call.message.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации")
        await bot.edit_message_media(file, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=menu)  

    elif call.data == "en-ru":
        await call.message.delete()
        await call.message.answer("Введите текст:") 
        await Users_text.user_translate_text_en_ru.set()
        await call.answer()

    elif call.data == "en-uz":
        await call.message.delete()
        await call.message.answer("Введите текст:") 
        await Users_text.user_translate_text_en_uz.set()
        await call.answer()

    elif call.data == "ru-en":
        await call.message.delete()
        await call.message.answer("Введите текст:") 
        await Users_text.user_translate_text_ru_en.set()
        await call.answer()
    
    elif call.data == "uz-en":
        await call.message.delete()
        await call.message.answer("Введите текст:") 
        await Users_text.user_translate_text_uz_en.set()
        await call.answer()

    
    elif call.data == "en-ru_img":
        await call.message.delete()
        await call.message.answer("Отправьте фото!") 
        await Users_text.user_translate_photo_en_ru.set()
        await call.answer()


    elif call.data == "en-uz_img":
        await call.message.delete()
        await call.message.answer("Отправьте фото!") 
        await Users_text.user_translate_photo_en_uz.set()
        await call.answer()


    elif call.data == "ru-en_img":
        await call.message.delete()
        await call.message.answer("Отправьте фото!") 
        await Users_text.user_translate_photo_ru_en.set()
        await call.answer()


    elif call.data == "uz-en_img":
        await call.message.delete()
        await call.message.answer("Отправьте фото!") 
        await Users_text.user_translate_photo_uz_en.set()
        await call.answer()
    

    elif call.data == "search_f":
        box_photo = "bot_for_b\\images\\poisk.jpg"
        file = types.InputMedia(media=types.InputFile(box_photo), caption=f"Введите имя <b>фильма</b>, <b>сериала</b>, <b>мультфильма</b> которую хотите посмотреть!")
        await bot.edit_message_media(file, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=back_to_menu) 
        await Names_media.media_name.set()

    elif call.data == "search_m":
        box_photo = "bot_for_b\images\searchm.jpg"
        file = types.InputMedia(media=types.InputFile(box_photo), caption=f"Введите имя <b>Песни</b> либо имя <b>Исполнителя</b> которую хотите услышать!")
        await bot.edit_message_media(file, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=back_to_menu) 
        await Names_media.voice_name.set()

    elif call.data == "first_button":
        cursor.execute("SELECT first_song FROM tgbot_multifunction WHERE user_id = %s;", ([call.message.chat.id]))
        values1 = cursor.fetchone()
        await bot.send_audio(call.message.chat.id, values1[0])

    elif call.data == "search_b":
        box_photo = "bot_for_b\images\searchb.jpg"
        file = types.InputMedia(media=types.InputFile(box_photo), caption=f"Введите имя <b>Книги</b> либо имя <b>Автора</b> которую хотите прочитать!")
        await bot.edit_message_media(file, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=back_to_menu) 
        await Names_media.bbook_name.set()

    elif call.data == "dow_v":
        box_photo = "bot_for_b\images\down.png"
        file = types.InputMedia(media=types.InputFile(box_photo), caption=f"⏹Выбирайте ту сеть, через которую хотите скачать видео!\n\nВ нашем боте есть три социальной сети: <b>Instagram</b>, <b>TikTok</b>, <b>Youtube</b>")
        await bot.edit_message_media(file, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=soc_media) 


    elif call.data == "Insta":
        box_photo = "bot_for_b\images\down.png"
        file = types.InputMedia(media=types.InputFile(box_photo), caption=f"🔗Отправьте нам ссылку видео из Инстаграмма, чтобы мы вам скачали видео!")
        await bot.edit_message_media(file, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=back_to_menu) 
        await Names_media.social_insta_link.set()

    elif call.data == "Yout":
        box_photo = "bot_for_b\images\down.png"
        file = types.InputMedia(media=types.InputFile(box_photo), caption=f"🔗Отправьте нам ссылку видео из Ютуба, чтобы мы вам скачали видео!")
        await bot.edit_message_media(file, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=back_to_menu) 
        await Names_media.social_yout_link.set()


    elif call.data == "mak_pr":
        await call.message.answer("Эта функция в разработке!")

@dp.callback_query_handler(text="first_button", state=Names_media.voice_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    cursor.execute("SELECT first_song FROM tgbot_multifunction WHERE user_id = %s;", ([call.message.chat.id]))
    values1 = cursor.fetchone()
    await bot.send_audio(call.message.chat.id, values1[0])
    await Names_media.voice_name.set()


@dp.callback_query_handler(text="secondd_button", state=Names_media.voice_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    cursor.execute("SELECT second_song FROM tgbot_multifunction WHERE user_id = %s;", ([call.message.chat.id]))
    values1 = cursor.fetchone()
    await bot.send_audio(call.message.chat.id, values1[0])
    await Names_media.voice_name.set()


@dp.callback_query_handler(text="third_button", state=Names_media.voice_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    cursor.execute("SELECT third_song FROM tgbot_multifunction WHERE user_id = %s;", ([call.message.chat.id]))
    values1 = cursor.fetchone()
    await bot.send_audio(call.message.chat.id, values1[0])
    await Names_media.voice_name.set()


@dp.callback_query_handler(text="fourth_button", state=Names_media.voice_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    cursor.execute("SELECT fourth_song FROM tgbot_multifunction WHERE user_id = %s;", ([call.message.chat.id]))
    values1 = cursor.fetchone()
    await bot.send_audio(call.message.chat.id, values1[0])
    await Names_media.voice_name.set()


@dp.callback_query_handler(text="fiveth_button", state=Names_media.voice_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    cursor.execute("SELECT fiveth_song FROM tgbot_multifunction WHERE user_id = %s;", ([call.message.chat.id]))
    values1 = cursor.fetchone()
    await bot.send_audio(call.message.chat.id, values1[0])
    await Names_media.voice_name.set()


@dp.callback_query_handler(text="sixth_button", state=Names_media.voice_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    cursor.execute("SELECT sixth_song FROM tgbot_multifunction WHERE user_id = %s;", ([call.message.chat.id]))
    values1 = cursor.fetchone()
    await bot.send_audio(call.message.chat.id, values1[0])
    await Names_media.voice_name.set()


@dp.callback_query_handler(text="seventh_button", state=Names_media.voice_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    cursor.execute("SELECT seventh_song FROM tgbot_multifunction WHERE user_id = %s;", ([call.message.chat.id]))
    values1 = cursor.fetchone()
    await bot.send_audio(call.message.chat.id, values1[0])
    await Names_media.voice_name.set()


@dp.callback_query_handler(text="eighth_button", state=Names_media.voice_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    cursor.execute("SELECT eighth_song FROM tgbot_multifunction WHERE user_id = %s;", ([call.message.chat.id]))
    values1 = cursor.fetchone()
    await bot.send_audio(call.message.chat.id, values1[0])
    await Names_media.voice_name.set()


@dp.callback_query_handler(text="nineth_button", state=Names_media.voice_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    cursor.execute("SELECT nineth_song FROM tgbot_multifunction WHERE user_id = %s;", ([call.message.chat.id]))
    values1 = cursor.fetchone()
    await bot.send_audio(call.message.chat.id, values1[0])
    await Names_media.voice_name.set()


@dp.callback_query_handler(text="tenth_button", state=Names_media.voice_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    cursor.execute("SELECT tenth_song FROM tgbot_multifunction WHERE user_id = %s;", ([call.message.chat.id]))
    values1 = cursor.fetchone()
    await bot.send_audio(call.message.chat.id, values1[0])
    await Names_media.voice_name.set()


@dp.callback_query_handler(text="back_menu", state=Names_media.voice_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)


@dp.callback_query_handler(text="back_menu", state=Users_text.user_translate_text_en_ru)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)



@dp.callback_query_handler(text="back_menu", state=Users_text.user_translate_text_en_uz)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)



@dp.callback_query_handler(text="back_menu", state=Users_text.user_translate_text_ru_en)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)


@dp.callback_query_handler(text="back_menu", state=Users_text.user_translate_text_uz_en)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)



@dp.callback_query_handler(text="back_menu", state=Users_text.user_translate_photo_en_ru)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)


@dp.callback_query_handler(text="back_menu", state=Users_text.user_translate_photo_ru_en)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)


@dp.callback_query_handler(text="back_menu", state=Users_text.user_translate_photo_en_uz)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)



@dp.callback_query_handler(text="back_menu", state=Users_text.user_translate_photo_uz_en)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)


@dp.callback_query_handler(text="back_menu", state=Names_media.media_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)


@dp.callback_query_handler(text="back_menu", state=Names_media.bbook_name)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)


@dp.callback_query_handler(text="back_menu", state=Names_media.social_insta_link)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)


@dp.callback_query_handler(text="back_menu", state=Names_media.social_yout_link)
async def back_to_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    box_photo = "bot_for_b\images\welcome.jpg" 
    photo_file = types.InputFile(box_photo)  
    await bot.send_photo(chat_id=call.message.chat.id, photo=photo_file, caption=f"👋Здравствуйте {call.from_user.full_name}, это многофункциональный бот который позволяет:\n\n1. Переводить\n2. Смотреть фильмы\n3. Слушать музыку\n4. Находить книгу\n5. Скачивать видео с разных площадок\n6. Делать презентации", reply_markup=menu)


@dp.message_handler(state=Users_text.user_translate_text_en_ru, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.full_name
    if types.ContentType.TEXT == message.content_type: 
        translation = translator.translate(message.text, dest="ru")
        await message.answer(translation.text, reply_markup=back_to_menu)

    else:
        await message.answer("Пожалуйста введите текст!")



@dp.message_handler(state=Users_text.user_translate_text_en_uz, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.full_name
    if types.ContentType.TEXT == message.content_type: 
        translation = translator.translate(message.text, dest="uz")
        await message.answer(translation.text, reply_markup=back_to_menu)

    else:
        await message.answer("Пожалуйста введите текст!")


@dp.message_handler(state=Users_text.user_translate_text_ru_en, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.full_name
    if types.ContentType.TEXT == message.content_type: 
        translation = translator.translate(message.text, dest="en")
        await message.answer(translation.text, reply_markup=back_to_menu)

    else:
        await message.answer("Пожалуйста введите текст!")


@dp.message_handler(state=Users_text.user_translate_text_uz_en, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.full_name
    if types.ContentType.TEXT == message.content_type: 
        translation = translator.translate(message.text, dest="en")
        await message.answer(translation.text, reply_markup=back_to_menu)

    else:
        await message.answer("Пожалуйста введите текст!")


@dp.message_handler(state=Users_text.user_translate_photo_en_ru, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.full_name
    if types.ContentType.PHOTO == message.content_type: 
        try:
            photo = message.photo[-1]
        
        # открываем фотографию без сохранения на диск
            photo_id = message.photo[-1].file_id

            # Получаем объект файла по идентификатору
            photo_file = await bot.get_file(photo_id)


        
            with io.BytesIO() as photo_stream:
                await photo_file.download(destination=photo_stream)
                image = Image.open(photo_stream)

                text = pytesseract.image_to_string(image=image, lang="eng")

                translation = translator.translate(text, dest="ru")
                await message.answer(translation.text, reply_markup=back_to_menu)

        except:
            pass

    else:
        await message.answer("Пожалуйста отправьте фото!")


@dp.message_handler(state=Users_text.user_translate_photo_en_uz, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.full_name
    if types.ContentType.PHOTO == message.content_type: 
        try:
            photo = message.photo[-1]
        
        # открываем фотографию без сохранения на диск
            photo_id = message.photo[-1].file_id

            # Получаем объект файла по идентификатору
            photo_file = await bot.get_file(photo_id)


        
            with io.BytesIO() as photo_stream:
                await photo_file.download(destination=photo_stream)
                image = Image.open(photo_stream)

                text = pytesseract.image_to_string(image=image, lang="eng")

                translation = translator.translate(text, dest="uz")
                await message.answer(translation.text, reply_markup=back_to_menu)

        except:
            pass

    else:
        await message.answer("Пожалуйста отправьте фото!")



@dp.message_handler(state=Users_text.user_translate_photo_ru_en, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.full_name
    if types.ContentType.PHOTO == message.content_type: 
        try:
            photo = message.photo[-1]
        
        # открываем фотографию без сохранения на диск
            photo_id = message.photo[-1].file_id

            # Получаем объект файла по идентификатору
            photo_file = await bot.get_file(photo_id)


        
            with io.BytesIO() as photo_stream:
                await photo_file.download(destination=photo_stream)
                image = Image.open(photo_stream)

                text = pytesseract.image_to_string(image=image, lang="rus")

                translation = translator.translate(text, dest="en")
                await message.answer(translation.text, reply_markup=back_to_menu)

        except:
            pass

    else:
        await message.answer("Пожалуйста отправьте фото!")




@dp.message_handler(state=Users_text.user_translate_photo_uz_en, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.full_name
    if types.ContentType.PHOTO == message.content_type: 
        try:
            photo = message.photo[-1]
        
        # открываем фотографию без сохранения на диск
            photo_id = message.photo[-1].file_id

            # Получаем объект файла по идентификатору
            photo_file = await bot.get_file(photo_id)


        
            with io.BytesIO() as photo_stream:
                await photo_file.download(destination=photo_stream)
                image = Image.open(photo_stream)

                text = pytesseract.image_to_string(image=image, lang="uzb")

                translation = translator.translate(text, dest="en")
                await message.answer(translation.text, reply_markup=back_to_menu)

        except:
            pass

    else:
        await message.answer("Пожалуйста отправьте фото!")



@dp.message_handler(state=Users_text.user_translate_photo_en_ru, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.full_name
    if types.ContentType.PHOTO == message.content_type: 
        try:
            photo = message.photo[-1]
        
        # открываем фотографию без сохранения на диск
            photo_id = message.photo[-1].file_id

            # Получаем объект файла по идентификатору
            photo_file = await bot.get_file(photo_id)


        
            with io.BytesIO() as photo_stream:
                await photo_file.download(destination=photo_stream)
                image = Image.open(photo_stream)

                text = pytesseract.image_to_string(image=image, lang="eng")

                translation = translator.translate(text, dest="ru")
                await message.answer(translation.text, reply_markup=back_to_menu)

        except:
            pass

    else:
        await message.answer("Пожалуйста отправьте фото!")





@dp.message_handler(state=Names_media.media_name, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.full_name
    if types.ContentType.TEXT == message.content_type: 
        await message.answer("Подождите, ваш запрос обрабатывается!")
        poster_caption = await search_media_files(message.text)
        box_photo = "bot_for_b\\images\\result.jpg"
        photo_file = types.InputFile(box_photo)
        await bot.send_photo(message.from_user.id, photo_file, caption=f"{poster_caption}", reply_markup=back_buttons)



    else:
        await message.answer("Пожалуйста отправьте текст!")




async def search_media_files(msg):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--lang=ru-RU")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument(f"userAgent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    driver.get("https://kinogo.biz/")

    time.sleep(1)
    search_input = driver.find_element(By.XPATH, "//input[@placeholder='Поиск...']")
    search_input.send_keys(msg)

    time.sleep(1)
    search_input.send_keys(Keys.ENTER)

    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    names = soup.find_all("div", class_="shortstory__title")
    links = OrderedDict()
    for link in driver.find_elements(By.TAG_NAME, "a"):
        href = link.get_attribute("href")
        if href == "https://kinogo.biz/top-filmy/":
            break

        else:
            if href.startswith("https://kinogo.biz/"):
                if len(href) >= 20 and href[19].isdigit():
                    links[href] = None


    description_text = "🔍В нашей базе нашлось несколько <b>Фильмов</b>, <b>Сериалов</b>, <b>Мультфильмов</b> с подобным названием:\n\n"
    if names:
        for number, name, link_media in zip(range(1, len(names)+1), names, links):
            description_text += f"🔺<b>[{number}]</b> <a href='{link_media}'>{name.text.strip()}</a>\n"

        description_text += "\n✍️ Если бот не нашел фильм которого хотите, перепроверьте название!"
        return description_text

    else:
        description_text = "😔Ничего не нашлось"
        return description_text



@dp.message_handler(state=Names_media.voice_name, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.id
    if types.ContentType.TEXT == message.content_type: 
        await message.answer("Подождите, ваш запрос обрабатывается!")
        search_audio = await get_music(message.text, user_name_full)
        search_result = "<b>Результаты 1-10</b>\n\n"
        if search_audio == "10":
            cursor.execute("SELECT first_song_text FROM tgbot_multifunction WHERE user_id = %s;", ([user_name_full]))
            values1 = cursor.fetchone()
            search_result += f"<b>1.</b> {values1[0]}\n"
            cursor.execute("SELECT second_song_text FROM tgbot_multifunction WHERE user_id = %s;", ([user_name_full]))
            values2 = cursor.fetchone()
            search_result += f"<b>2.</b> {values2[0]}\n"
            cursor.execute("SELECT third_song_text FROM tgbot_multifunction WHERE user_id = %s;", ([user_name_full]))
            values3 = cursor.fetchone()
            search_result += f"<b>3.</b> {values3[0]}\n"
            cursor.execute("SELECT fourth_song_text FROM tgbot_multifunction WHERE user_id = %s;", ([user_name_full]))
            values4 = cursor.fetchone()
            search_result += f"<b>4.</b> {values4[0]}\n"
            cursor.execute("SELECT fiveth_song_text FROM tgbot_multifunction WHERE user_id = %s;", ([user_name_full]))
            values5 = cursor.fetchone()
            search_result += f"<b>5.</b> {values5[0]}\n"
            cursor.execute("SELECT sixth_song_text FROM tgbot_multifunction WHERE user_id = %s;", ([user_name_full]))
            values6 = cursor.fetchone()
            search_result += f"<b>6.</b> {values6[0]}\n"
            cursor.execute("SELECT seventh_song_text FROM tgbot_multifunction WHERE user_id = %s;", ([user_name_full]))
            values7 = cursor.fetchone()
            search_result += f"<b>7.</b> {values7[0]}\n"
            cursor.execute("SELECT eighth_song_text FROM tgbot_multifunction WHERE user_id = %s;", ([user_name_full]))
            values8 = cursor.fetchone()
            search_result += f"<b>8.</b> {values8[0]}\n"
            cursor.execute("SELECT nineth_song_text FROM tgbot_multifunction WHERE user_id = %s;", ([user_name_full]))
            values9 = cursor.fetchone()
            search_result += f"<b>9.</b> {values9[0]}\n"
            cursor.execute("SELECT tenth_song_text FROM tgbot_multifunction WHERE user_id = %s;", ([user_name_full]))
            values10 = cursor.fetchone()
            search_result += f"<b>10.</b> {values10[0]}\n"
            await message.answer(search_result, reply_markup=menu_for_audios)

        elif search_audio == "1":
            cursor.execute("SELECT first_song FROM tgbot_multifunction WHERE user_id = %s;", ([user_name_full]))
            values = cursor.fetchone()
            await bot.send_audio(message.from_user.id, audio=values[0])

        elif search_audio == "0":
            await message.answer("😔Ничего не нашлось", reply_markup=back_buttons)

    else:
        await message.answer("Пожалуйста отправьте текст!")


async def get_music(title_music, tg_user_id):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--lang=ru-RU")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("userAgent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    driver.get("https://megapesni.com/")
    time.sleep(1)

    search_input = driver.find_element(By.CLASS_NAME, "form-search.ui-autocomplete-input")
    search_input.send_keys(title_music)
    search_input.send_keys(Keys.ENTER)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    link_for_audio = soup.find_all("a", class_="popular-play__item")
    names = soup.find_all("div", class_="popular-play-name")

    if len(link_for_audio) > 10:
        for link, name, num_songs in zip(link_for_audio, names, range(1, 11)):
            music_link = link["data-url"]
            music_name = name.text
            if num_songs == 1:
                cursor.execute("UPDATE tgbot_multifunction SET first_song = %s WHERE user_id = %s;", ([music_link, tg_user_id]))
                cursor.execute("UPDATE tgbot_multifunction SET first_song_text = %s WHERE user_id = %s;", ([music_name, tg_user_id]))
                connection.commit() 

            elif num_songs == 2:
                cursor.execute("UPDATE tgbot_multifunction SET second_song = %s WHERE user_id = %s;", ([music_link, tg_user_id]))
                cursor.execute("UPDATE tgbot_multifunction SET second_song_text = %s WHERE user_id = %s;", ([music_name, tg_user_id]))
                connection.commit() 

            elif num_songs == 3:
                cursor.execute("UPDATE tgbot_multifunction SET third_song = %s WHERE user_id = %s;", ([music_link, tg_user_id]))
                cursor.execute("UPDATE tgbot_multifunction SET third_song_text = %s WHERE user_id = %s;", ([music_name, tg_user_id]))
                connection.commit() 

            elif num_songs == 4:
                cursor.execute("UPDATE tgbot_multifunction SET fourth_song = %s WHERE user_id = %s;", ([music_link, tg_user_id]))
                cursor.execute("UPDATE tgbot_multifunction SET fourth_song_text = %s WHERE user_id = %s;", ([music_name, tg_user_id]))
                connection.commit() 

            elif num_songs == 5:
                cursor.execute("UPDATE tgbot_multifunction SET fiveth_song = %s WHERE user_id = %s;", ([music_link, tg_user_id]))
                cursor.execute("UPDATE tgbot_multifunction SET fiveth_song_text = %s WHERE user_id = %s;", ([music_name, tg_user_id]))
                connection.commit() 

            elif num_songs == 6:
                cursor.execute("UPDATE tgbot_multifunction SET sixth_song = %s WHERE user_id = %s;", ([music_link, tg_user_id]))
                cursor.execute("UPDATE tgbot_multifunction SET sixth_song_text = %s WHERE user_id = %s;", ([music_name, tg_user_id]))
                connection.commit() 

            elif num_songs == 7:
                cursor.execute("UPDATE tgbot_multifunction SET seventh_song = %s WHERE user_id = %s;", ([music_link, tg_user_id]))
                cursor.execute("UPDATE tgbot_multifunction SET seventh_song_text = %s WHERE user_id = %s;", ([music_name, tg_user_id]))
                connection.commit() 

            elif num_songs == 8:
                cursor.execute("UPDATE tgbot_multifunction SET eighth_song = %s WHERE user_id = %s;", ([music_link, tg_user_id]))
                cursor.execute("UPDATE tgbot_multifunction SET eighth_song_text = %s WHERE user_id = %s;", ([music_name, tg_user_id]))
                connection.commit() 

            elif num_songs == 9:
                cursor.execute("UPDATE tgbot_multifunction SET nineth_song = %s WHERE user_id = %s;", ([music_link, tg_user_id]))
                cursor.execute("UPDATE tgbot_multifunction SET nineth_song_text = %s WHERE user_id = %s;", ([music_name, tg_user_id]))
                connection.commit() 

            elif num_songs == 10:
                cursor.execute("UPDATE tgbot_multifunction SET tenth_song = %s WHERE user_id = %s;", ([music_link, tg_user_id]))
                cursor.execute("UPDATE tgbot_multifunction SET tenth_song_text = %s WHERE user_id = %s;", ([music_name, tg_user_id]))
                connection.commit() 

        return "10"

    elif len(link_for_audio) > 0:
        cursor.execute("UPDATE tgbot_multifunction SET first_song = %s WHERE user_id = %s;", ([music_link, tg_user_id]))
        return "1"

    
    else:
        return "0"


@dp.message_handler(state=Names_media.bbook_name, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.id
    if types.ContentType.TEXT == message.content_type:
        await message.answer("Подождите, ваш запрос обрабатывается!")
        search_book = await get_book(message.text)
        if search_book != 0:
            box_photo = "bot_for_b\\images\\result.jpg"
            photo_file = types.InputFile(box_photo)
            await bot.send_photo(message.from_user.id, photo_file, caption=f"{search_book}", reply_markup=back_buttons)

        elif search_book == 0:
            box_photo = "bot_for_b\\images\\result.jpg"
            photo_file = types.InputFile(box_photo)
            await bot.send_photo(message.from_user.id, photo_file, caption=f"{search_book}", reply_markup=back_buttons)


    else:
        await message.answer("Пожалуйста отправьте текст!")

async def get_book(title_book):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--lang=ru-RU")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("userAgent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    driver.get("https://avidreaders.ru/")
    time.sleep(1)

    search_input = driver.find_element(By.CSS_SELECTOR, "input[id='search-txt']")
    search_input.send_keys(title_book)
    search_input.send_keys(Keys.ENTER)
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    link_for_book = soup.find_all("a", class_="btn")
    names = soup.find_all("div", class_="book_name")

    if len(link_for_book) > 10:
        books_results =  "🔍В нашей базе нашлось несколько <b>Книг</b> с подобным названием:\n\n"
        for link, name, num_songs in zip(link_for_book, names, range(1, 11)):
            book_link = link["href"]
            book_name = name.text
            books_results += f"🔺<b>[{num_songs}]</b> <a href='{book_link}'>{book_name.strip()}</a>\n"

        books_results += "\n✍️ Если бот не нашел книгу которого хотите, перепроверьте название!"
        return books_results

    elif len(link_for_book) > 0:
        books_results =  "🔍В нашей базе нашлось несколько <b>Книг</b> с подобным названием:\n\n"
        for link, name, num_songs in zip(link_for_book, names, range(1, len(link_for_book)+1)):
            book_link = link["href"]
            book_name = name.text
            books_results += f"🔺<b>[{num_songs}]</b> <a href='{book_link}'>{book_name.strip()}</a>\n"

        books_results += "\n✍️ Если бот не нашел книгу которого хотите, перепроверьте название!"
        return books_results

    else:
        return "0"



@dp.message_handler(state=Names_media.social_insta_link, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.id
    if types.ContentType.TEXT == message.content_type:
        if message.text.startswith("https://www.instagram.com/"):
            await message.answer("Подождите, ваш запрос обрабатывается!")
            video_insta_url = await download_insta_func(message.text)
            if video_insta_url != "0":
                await bot.send_video(user_name_full, video_insta_url, caption="Спасибо, что пользуетесь - <a href='https://t.me/send_to_90bot'>Рассылщиком</a>", reply_markup=back_to_menu)

            else:
                await bot.send_message(message.from_user.id, "Пожалуйста перепроверьте отправленную ссылку!")

        else:
            await message.answer("Пожалуйста отправьте правильную ссылку!")

    else:
        await message.answer("Пожалуйста отправьте текст!")


async def download_insta_func(url_video):

    url = "https://instagram-post-and-reels-downloader.p.rapidapi.com/insta/"

    querystring = {"url":url_video}

    headers = {
        "X-RapidAPI-Key": "51efbfb617mshfe027eb5782a110p14e4a0jsn11c17cc1bd33",
        "X-RapidAPI-Host": "instagram-post-and-reels-downloader.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    try:
        insta_video = data['detail']['data']['items'][0]['urls'][0]['urlWrapped']
        return insta_video

    except:
        return '0'



@dp.message_handler(state=Names_media.social_yout_link, content_types=types.ContentType.ANY) 
async def mail_on(message: types.Message, state: FSMContext): 
    user_name_full = message.from_user.id
    if types.ContentType.TEXT == message.content_type:
        if message.text.startswith("https://www.youtube.com/shorts"):
            match = re.search(r"https://www.youtube.com/shorts/(.*)", message.text)
            text = match.group(1)
            await message.answer("Подождите, ваш запрос обрабатывается!")
            video_yout_url = await get_youtube_video(text)
            if video_yout_url != "0":
                await bot.send_video(user_name_full, video_yout_url, caption="Спасибо, что пользуетесь - <a href='https://t.me/send_to_90bot'>Рассылщиком</a>", reply_markup=back_to_menu)

            else:
                await bot.send_message(message.from_user.id, "Пожалуйста перепроверьте отправленную ссылку!")

        else:
            await message.answer("Этот бот скачивает только шортс видео, пожалуйста отправьте правильную ссылку!")

    else:
        await message.answer("Пожалуйста отправьте текст!")

async def get_youtube_video(id_y_video):
    url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"

    querystring = {"id":id_y_video}

    headers = {
        "X-RapidAPI-Key": "51efbfb617mshfe027eb5782a110p14e4a0jsn11c17cc1bd33",
        "X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    y_video = response.json()
    try:
        video_url = y_video["formats"][0]['url']

        return video_url

    except:
        return "0"


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)