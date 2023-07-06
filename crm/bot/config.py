import os

from django.conf import settings
from dotenv import load_dotenv
from telebot import TeleBot

load_dotenv()


bot = TeleBot(settings.TELEGRAM_API_TOKEN, threaded=False)
