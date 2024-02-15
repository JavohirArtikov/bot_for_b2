from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🇬🇧Переводчик", callback_data="transl"),
        InlineKeyboardButton(text="🎞Поиск фильма", callback_data="search_f")
    ],
    [
        InlineKeyboardButton(text="🎵Поиск песен", callback_data="search_m"),
        InlineKeyboardButton(text="📚Поиск книг", callback_data="search_b")
    ],
    [
        InlineKeyboardButton(text="📹Скачать видео", callback_data="dow_v"),
        InlineKeyboardButton(text="📑Сделать презентацию", callback_data="mak_pr")
    ], 
    ]
)




inline_translation = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💬Через текст", callback_data="with_text"),
            InlineKeyboardButton(text="📷Через картинку", callback_data="with_img")
        ],
        [
            InlineKeyboardButton(text="◀️Назад", callback_data="back")
        ]
    ]
)



inline_translation_text = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇬🇧-🇷🇺", callback_data="en-ru"),
            InlineKeyboardButton(text="🇬🇧-🇺🇿", callback_data="en-uz")
        ],
        [
            InlineKeyboardButton(text="🇷🇺-🇬🇧", callback_data="ru-en"),
            InlineKeyboardButton(text="🇺🇿-🇬🇧", callback_data="uz-en")
        ],
        [
            InlineKeyboardButton(text="◀️Назад", callback_data="back_translation")
        ]
    ]
)



inline_translation_img = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇬🇧-🇷🇺", callback_data="en-ru_img"),
            InlineKeyboardButton(text="🇬🇧-🇺🇿", callback_data="en-uz_img")
        ],
        [
            InlineKeyboardButton(text="🇷🇺-🇬🇧", callback_data="ru-en_img"),
            InlineKeyboardButton(text="🇺🇿-🇬🇧", callback_data="uz-en_img")
        ],
        [
            InlineKeyboardButton(text="◀️Назад", callback_data="back_translation")
        ]
    ]
)


back_to_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️Меню", callback_data="back_menu")
        ]
    ]
)


back_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="◀️Меню", callback_data="back_menu")
        ]
    ]
)


menu_for_audios = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data="first_button"),
            InlineKeyboardButton(text="2", callback_data="secondd_button"),
            InlineKeyboardButton(text="3", callback_data="third_button"),
            InlineKeyboardButton(text="4", callback_data="fourth_button"),
            InlineKeyboardButton(text="5", callback_data="fiveth_button"),
        ],
        [
            InlineKeyboardButton(text="6", callback_data="sixth_button"),
            InlineKeyboardButton(text="7", callback_data="seventh_button"),
            InlineKeyboardButton(text="8", callback_data="eighth_button"),
            InlineKeyboardButton(text="9", callback_data="nineth_button"),
            InlineKeyboardButton(text="10", callback_data="tenth_button"),
        ],
        [
            InlineKeyboardButton(text="◀️Меню", callback_data="back_menu")
        ]
    ]
)



soc_media = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🌐Instagram", callback_data="Insta"),
            InlineKeyboardButton(text="🌐Youtube", callback_data="Yout")
        ],
        [
            InlineKeyboardButton(text="◀️Меню", callback_data="back_menu")
        ]
    ]
)