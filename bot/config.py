import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)

logging.basicConfig(level=logging.INFO)
