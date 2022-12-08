import aiogram
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API  #авторизационный токен для подключения к телеграм API перенесен в отдельный файл config.py
import string
import random

# бот это сервер который будет взаимодействовать с API Telegram

HELP_COMMAND = """
/help - список комманд
/start - начать работу с ботом
""" # Создал новую переменную для описания списка команд что бы не переписывать их в функцию


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)



if __name__ == '__main__':
    executor.start_polling(dp)
