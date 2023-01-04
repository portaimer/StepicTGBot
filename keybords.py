from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove #Импртируем классы для создания клавиатуры
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


#Инлайн клавиатура
ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='VK Создателя',
                           url="https://vk.com/id306646249")

ib2 = InlineKeyboardButton(text='Github Создателя',
                           url="https://github.com/portaimer")
ikb.add(ib1, ib2)


