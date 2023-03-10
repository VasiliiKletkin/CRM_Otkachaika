import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = os.environ.get("API_TOKEN")

bot = Bot(token=API_TOKEN)
memory_storage = MemoryStorage()
dp = Dispatcher(bot, storage=memory_storage)

logging.basicConfig(level=logging.INFO)
