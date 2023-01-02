import logging
from aiogram import Bot, Dispatcher, executor, types
import os

from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    text = "Привет это бот Откачайка для водителей" \
        "Вы можете смотреть все заказы, выполнять их и тд" \
        "Все функции указаны на клавиатуре"
    await message.reply(text)

@dp.message_handler()
async def menu(message: types.Message):

    await message.answer(message.text)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
