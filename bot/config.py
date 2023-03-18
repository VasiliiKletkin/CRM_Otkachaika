import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv()

API_TOKEN = os.environ.get("API_TOKEN")
TIME_UPDATE_ORDERS = os.environ.get("TIME_UPDATE_ORDERS", 10)

bot = Bot(token=API_TOKEN)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)

logging.basicConfig(level=logging.INFO)
