
from bot import handlers
from bot.callbacks import bind_filters
from bot.config import bot
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Implemented to Django application telegram bot setup command'

    def handle(self, *args, **kwargs):
        bind_filters(bot=bot)
        bot.enable_save_next_step_handlers(delay=2) # Сохранение обработчиков
        bot.load_next_step_handlers()								# Загрузка обработчиков
        bot.infinity_polling()											# Бесконечный цикл бота
