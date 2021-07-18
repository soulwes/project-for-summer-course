from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

euro_btn = KeyboardButton('Курс Евро')
dollar_btn = KeyboardButton('Курс Доллара США')
bank_btn = KeyboardButton('Ближайшие банки', request_location=True)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(euro_btn, dollar_btn).add(bank_btn)
