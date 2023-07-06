from crm.celery import app

from .keyboards import get_order_inline_keyboard
from .utils import get_order_info


@app.task
def send_order_to_driver(order_id):
    from bot.management.commands.bot import bot
    from orders.models import Order

    order = Order.objects.get(id=order_id)
    try:
        bot.send_message(
            chat_id=order.driver.profile.telegram.user_id,
            text=get_order_info(order),
            reply_markup=get_order_inline_keyboard(order),
        )
        order.is_sent = True
        order.save()
    except:
        pass
