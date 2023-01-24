import aiogram
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove  # Импртируем классы для создания клавиатуры
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from keybords import ikb
import asyncio
from aiogram.utils.exceptions import BotBlocked #Ипортируем для проверки заблокирован ли бот


# бот это сервер который будет взаимодействовать с API Telegram

TOKEN_API  # авторизационный токен для подключения к телеграм API перенесен в отдельный файл config.py
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот был успешно запущен')


HELP_COMMAND = """
<b>/help</b> - <em>список комманд</em>
<b>/give</b> - <em>отправить gifку</em>
<b>/start</b> - <em>вызвать клавиатуру</em>
<b>Отправь боту стикер</b> - <em>получишь id стикера</em>
<b>/image</b> - <em>Получить картинку</em>
<b>/location</b> - <em>Получить координаты пока что просто статичные координаты, бот еще в разработке </em>
<b>/creator</b> - <em>Creator</em>
"""  # Создал новую переменную для описания списка команд что бы не переписывать их в функцию

# Пилим клавиатуру для пользователя
kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         # Для того что бы клавиатура меняла свой размер в зависимости от устройстваю)
                         one_time_keyboard=True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/give')
b3 = KeyboardButton('/image')
b4 = KeyboardButton('/location')
b5 = KeyboardButton('/creator')
b6 = KeyboardButton('/vote')
kb.add(b1, b2, b3, b5, b6)


@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    ikb2 = InlineKeyboardMarkup(row_width=2)
    ib2_1 = InlineKeyboardButton(text='👍',
                                 callback_data='like')
    ib2_2 = InlineKeyboardButton(text='👎',
                                 callback_data='dislike')
    ikb2.add(ib2_1, ib2_2)

    await bot.send_photo(chat_id=message.from_user.id,
                         photo=types.InputFile.from_url('https://bing.ioliu.cn/v1/rand'),
                         caption='Как тебе фото ?',
                         reply_markup=ikb2)


@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'Like':
        await callback.answer('Отлично')
    await callback.answer('Тебе не нравиться? А я ведь так старался ...')


@dp.message_handler(commands=['creator'])
async def creator(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Где найти меня в сети',
                           parse_mode="HTML",
                           reply_markup=ikb)
    await message.delete()


@dp.message_handler(commands=['start'])  # Автоматическое приветствие на команду /start
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Привет Приятно Познакомиться Я FreePizzzza Bot, сейчас у вас появиться клавиатура она подскажет как со мной работать ',
                           parse_mode="HTML",
                           reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])  # По команде /help  возвращает список команд HELP_COMMAND в личку пользователю
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML", )
    await message.delete()


@dp.message_handler(content_types=['sticker'])  # Отправляет обратно айди стикера по входящему стикеру
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)
    await message.delete()


@dp.message_handler(commands=['image'])  # Получаем случйное изображение
async def cmd_image(message: types.Message):
    await bot.send_photo(message.chat.id, types.InputFile.from_url('https://bing.ioliu.cn/v1/rand'))
    await message.delete()


@dp.message_handler(commands=['give'])  # Отправка стикера на команду give
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAEG5RVjoLxDtsexaNuvodBr4kEh-TphBwACTRYAAnJ3wEiqLAI1EPSbGSwE")
    await message.delete()  # Просто удалит сообщение от пользователя что бы не было много спама


@dp.errors_handler(exception=BotBlocked) #Функция проверки заблокировали бот
async def error_bot_bloked_hendler(updeta: types.Update, exception: BotBlocked) ->bool:
    print("Нас заблокировали")
    return True

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
