from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

ORDERS = 'ЗАКАЗЫ'
MAIN_MENU = (
    (ORDERS, "orders" ),
)

inprogress_call_back = CallbackData('INPROGRESS', 'order_id')
completed_call_back = CallbackData('COMPLETED', 'order_id')
canceled_call_back = CallbackData('CANCELED', 'order_id')


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1)
    for button in MAIN_MENU:
        keyboard.add(KeyboardButton(button))
    return keyboard

def inline_order_keyboard(order)->InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    in_progress_button = InlineKeyboardButton('Начать', callback_data=inprogress_call_back.new(order_id=order['id']))
    completed_button = InlineKeyboardButton('Завершить', callback_data=completed_call_back.new(order_id=order['id']))
    canceled_button = InlineKeyboardButton('Отменить', callback_data=canceled_call_back.new(order_id=order['id']))

    status = order['status']
    if status == "CONFIRMED":
        return keyboard.add(in_progress_button)
    if status == "INPROGRESS":
        return keyboard.add(completed_button).add(canceled_button)

def not_available_orders_keyboard()->InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    update_button = InlineKeyboardButton('Обновить', callback_data='UPDATE')
    return keyboard.add(update_button)