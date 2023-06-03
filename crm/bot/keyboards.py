from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from .callbacks import order_callback


def get_order_inline_keyboard(order):
    keyboard = InlineKeyboardMarkup()
    start_button = InlineKeyboardButton(
        'Начать', callback_data=order_callback.new(order_id=order.id, button="start"))
    complete_button = InlineKeyboardButton(
        'Завершить', callback_data=order_callback.new(order_id=order.id, button="complete"))
    cancel_button = InlineKeyboardButton(
        'Отменить', callback_data=order_callback.new(order_id=order.id, button="cancel"))
    status = order.status
    if status == "CONFIRMED":
        return keyboard.add(start_button)
    elif status == "INPROGRESS":
        return keyboard.add(complete_button).add(cancel_button)