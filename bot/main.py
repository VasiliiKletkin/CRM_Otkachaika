import logging
from aiogram import Bot, Dispatcher, executor
import handlers
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
