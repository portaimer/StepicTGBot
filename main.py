import aiogram
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API  #авторизационный токен для подключения к телеграм API перенесен в отдельный файл config.py
import string
import random

# бот это сервер который будет взаимодействовать с API Telegram

HELP_COMMAND = """
<b>/help</b> - <em>список комманд</em>
<b>/give</b> - <em>отправить gifку</em>
<b>/start</b> - <em>начать работу с ботом</em>
<b>Отправь боту стикер</b> - <em>получишь id стикера</em>
"""# Создал новую переменную для описания списка команд что бы не переписывать их в функцию


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот был успешно запущен')

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=HELP_COMMAND, parse_mode='HTML')
    await message.delete()


@dp.message_handler(content_types=['sticker'])#Отправляет обратно айди стикера по входящему стикеру
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)


#@dp.message_handler(commands=['start']) #Автоматическое приветствие на команду /start
#async def start_command(message: types.Message):
    #await message.answer('<em>Привет, добро пожаловать в наш бот!</em>', parse_mode="HTML")

@dp.message_handler(commands=['give']) #Отправка стикера на команду give
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEG5RVjoLxDtsexaNuvodBr4kEh-TphBwACTRYAAnJ3wEiqLAI1EPSbGSwE")
    await message.delete()# Просто удалит сообщение от пользователя что бы не было много спама

#@dp.message_handler() #эхо бот + эмодзи с авто удалением сообщения
#async def send_emoji(message: types.Message):
    #await message.reply(message.text + '👍')
    #await message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
