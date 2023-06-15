from bot.keyboards import get_order_inline_keyboard
from bot.utils import get_order_info

from crm.celery import app


@app.task
def send_order_to_driver(order_id):
    from bot.management.commands.bot import bot
    from .models import Order
    order = Order.objects.get(id=order_id)
    try:
        bot.send_message(order.driver.profile.telegram.user_id, get_order_info(order), reply_markup=get_order_inline_keyboard(order))
        order.is_sent = True
        order.save()
    except:
        pass