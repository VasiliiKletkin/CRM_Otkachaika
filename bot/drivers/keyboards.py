from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)

from .callbacks import order_call_back

ORDERS = 'ЗАКАЗЫ'
MAIN_MENU = (
    # ORDERS,
)


def inline_order_keyboard(order) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    in_progress_button = InlineKeyboardButton(
        'Начать', callback_data=order_call_back.new(status="INPROGRESS", order_id=order['id']))
    completed_button = InlineKeyboardButton(
        'Завершить', callback_data=order_call_back.new(status="COMPLETED", order_id=order['id']))
    canceled_button = InlineKeyboardButton(
        'Отменить', callback_data=order_call_back.new(status="CANCELED", order_id=order['id']))

    status = order['status']
    if status == "CONFIRMED":
        return keyboard.add(in_progress_button)
    elif status == "INPROGRESS":
        return keyboard.add(completed_button).add(canceled_button)


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1)
    for button in MAIN_MENU:
        keyboard.add(KeyboardButton(button))
    return keyboard
