# from datetime import datetime

# from django.db.models import Q
# from orders.models import Order
# from telebot import types

# from crm.celery import app

# from .callbacks import order_callback
# from .keyboards import get_order_inline_keyboard
# from .management.commands.bot import bot
# from .utils import get_order_info


# # @app.task
# # def send_message(telegram_id, message):
# #     bot.send_message(telegram_id, message)


# # @app.task
# # def send_orders_today():
# #     current_datetime = datetime.today()
# #     orders = Order.objects.filter(Q(date_planned__date__lte=current_datetime) | Q(
# #         date_planned__isnull=True), status__in=[Order.CONFIRMED, Order.INPROGRESS], is_sent=False, driver__profile__telegram__is_null=False)
    
# #     for order in orders:
# #         send_message.delay(order.driver.profile.telegram.user_id, get_order_info(order), reply_markup=get_order_inline_keyboard(order))
# #     orders.update(is_sent=True)

