import keys_TG
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Location, ContentTypes
import keyboard
from pars import rate, bank
bot = Bot(keys_TG.token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет!\n'
                         'Бот берет курс доллара и евро с сайта Тинькофф\n'
                         'Ближайшие банки ищет в GoogleMaps',
                         reply_markup=keyboard.main_menu)


@dp.message_handler(commands=['help'])
async def help_user(message):
    await message.answer('Я могу подсказать тебе нынешний курс Доллара и Евро,\n'
                         'Показать Банки в радиусе двух километров')


@dp.message_handler(lambda x: x.text == 'Курс Доллара США')
async def dollar_rate(message):
    prev = rate.prev_dollar
    new = rate.exchange_dol()
    m = f'Текущий курс: {rate.exchange_dol()} рубля за доллар\n'
    if prev != 0:
        m += f'С момента прошлого запроса цена изменилась на {((new-prev)/prev)*100}%'
    else:
        m += 'Чтобы получить аналитику, по изменению цены, запросите курс доллара повторно.'
    await message.reply(m)


@dp.message_handler(lambda x: x.text == 'Курс Евро')
async def euro_rate(message):
    prev = rate.prev_euro
    new = rate.exchange_eu()
    m = f'Текущий курс: {rate.exchange_eu()} рубля за евро\n'
    if prev != 0:
        m += f'С момента прошлого запроса цена изменилась на {((new-prev)/prev)*100}%'
    else:
        m += 'Чтобы получить аналитику, по изменению цены, запросите курс евро повторно.'
    await message.reply(m)


@dp.message_handler(lambda x: x.text == 'Ближайший банк')
async def not_geolocation(message):
    await message.reply('Отправьте геопозицию')


@dp.message_handler(content_types=ContentTypes.LOCATION)
async def geolocation(message: Location):
    coord = f"{message.location.latitude},{message.location.longitude}"
    s = bank.near_bank(coord)
    if s == '':
        await message.reply('К сожалению рядом с вами нет банков')
    else:
        await message.reply(s)


executor.start_polling(dp)
