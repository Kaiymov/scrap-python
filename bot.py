from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

import os

bot = Bot('5664915637:AAGLY1LR_AJ3xQnRNN-NeYhmGck6qqL8Nsw')
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = KeyboardButton(text='/how_many')
kb.add(kb1)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Welcome', reply_markup=kb)


@dp.message_handler(commands=['how_many'])
async def cmd_how_many(message: types.Message):
    with open('bot_send.txt', 'r') as file:
        file = file.read().split()[0]

    if file == '61':
        await message.answer(text='Загрузка заершена')
        await message.reply_document(open('seconom24.xlsx', 'rb'))
    else:
        await message.answer(text=file, reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)

