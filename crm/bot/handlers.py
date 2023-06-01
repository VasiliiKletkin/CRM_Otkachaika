


from bot.callbacks import order_callback
from bot.config import bot
from bot.keyboards import get_order_inline_keyboard

from bot.utils import get_order_info
from orders.models import Order
from telebot import types
from users.models import Telegram


@bot.message_handler(commands=['start',])
def send_welcome(message):
  bot.send_message(message.chat.id, "Это бот Откачайкаа")
  obj, created = Telegram.objects.update_or_create(
    user_id=message.from_user.id,
    defaults={"username": message.from_user.username,
               "first_name": message.from_user.first_name,
               "last_name": message.from_user.last_name
               }
    )

@bot.callback_query_handler(func=None, order_config=order_callback.filter(button="start"))
def order_callback_started(call: types.CallbackQuery):
    callback_data: dict = order_callback.parse(callback_data=call.data)
    order = Order.objects.get(id=callback_data['order_id'])
    order.status = Order.INPROGRESS
    order.save()
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=get_order_info(order), reply_markup=get_order_inline_keyboard(order))
    
@bot.callback_query_handler(func=None, order_config=order_callback.filter(button="complete"))
def order_callback_completed(call: types.CallbackQuery):
    callback_data: dict = order_callback.parse(callback_data=call.data)
    order = Order.objects.get(id=callback_data['order_id'])
    order.status = Order.COMPLETED
    order.save()
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=get_order_info(order), reply_markup=get_order_inline_keyboard(order))


@bot.callback_query_handler(func=None, order_config=order_callback.filter(button="cancel"))
def callback_order_canceled(call: types.CallbackQuery):
    callback_data: dict = order_callback.parse(callback_data=call.data)
    order = Order.objects.get(id=callback_data['order_id'])
    order.status = Order.CANCELED
    order.save()
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=get_order_info(order), reply_markup=get_order_inline_keyboard(order))
