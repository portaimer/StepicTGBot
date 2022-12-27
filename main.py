import aiogram
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API  #авторизационный токен для подключения к телеграм API перенесен в отдельный файл config.py
import string
import random
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove #Импртируем классы для создания клавиатуры
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# бот это сервер который будет взаимодействовать с API Telegram

HELP_COMMAND = """
<b>/help</b> - <em>список комманд</em>
<b>/give</b> - <em>отправить gifку</em>
<b>/start</b> - <em>вызвать клавиатуру</em>
<b>Отправь боту стикер</b> - <em>получишь id стикера</em>
<b>/image</b> - <em>Получить картинку</em>
<b>/location</b> - <em>Получить координаты </em>
<b>/creator</b> - <em>Creator</em>
"""# Создал новую переменную для описания списка команд что бы не переписывать их в функцию


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот был успешно запущен')


#Пилим клавиатуру для пользователя
kb = ReplyKeyboardMarkup(resize_keyboard=True,)#Для того что бы клавиатура меняла свой размер в зависимости от устройстваю)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/give')
b3 = KeyboardButton('/image')
b4 = KeyboardButton('/location')
kb.add(b1, b2, b3, b4,)


#Инлайн клавиатура
ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='VK Создателя',
                          url="https://vk.com/id306646249")

ib2 = InlineKeyboardButton(text='Github Создателя',
                           url="https://github.com/portaimer")
ikb.add(ib1,ib2)

@dp.message_handler(commands=['creator'])
async def creator(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Где найти меня в сети',
                           parse_mode="HTML",
                           reply_markup=ikb)


#@dp.message_handler()#Эхо бот
#async def echo(message: types.Message):
    #await bot.send_message(chat_id=message.from_user.id, text="Hello")#Бот присылает сообщение в личку пользователю

#@dp.message_handler(commands=['help'])
#async def help_command(message: types.Message):
    #await message.reply(text=HELP_COMMAND, parse_mode="HTML")
    #await message.delete()


@dp.message_handler(commands=['start']) #Автоматическое приветствие на команду /start
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Привет Приятно Познакомиться Я FreePizzzza Bot, сейчас у вас появиться клавиатура она подскажет как со мной работать ',
                           parse_mode="HTML",)
    await message.delete()


@dp.message_handler(commands=['help'])#По команде /help  возвращает список команд HELP_COMMAND в личку пользователю
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML",)
    await message.delete()


@dp.message_handler(content_types=['sticker'])#Отправляет обратно айди стикера по входящему стикеру
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)
    await message.delete()


@dp.message_handler(commands=['image'])#Получаем случйное изображение
async def cmd_image(message: types.Message):
    await bot.send_photo(message.chat.id, types.InputFile.from_url('https://bing.ioliu.cn/v1/rand'))
    await message.delete()


@dp.message_handler(commands=['location'])#Бот присылает локацию в личку из чата
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude='55',
                            longitude=74)


@dp.message_handler(commands=['give']) #Отправка стикера на команду give
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEG5RVjoLxDtsexaNuvodBr4kEh-TphBwACTRYAAnJ3wEiqLAI1EPSbGSwE")
    await message.delete()# Просто удалит сообщение от пользователя что бы не было много спама

#@dp.message_handler() #эхо бот + эмодзи с авто удалением сообщения
#async def send_emoji(message: types.Message):
    #await message.reply(message.text + '👍')
    #await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
