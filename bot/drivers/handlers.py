from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from config import dp
from drivers.api import canceled_order, completed_order, started_order
from utils import is_driver

from .keyboards import (ORDERS, canceled_call_back, completed_call_back,
                        in_progress_call_back, inline_order_keyboard,
                        main_menu_keyboard)


@dp.message_handler(commands=['start', 'help'])
async def start(message: Message):
    if is_driver(message.chat.id):
        text = "Привет это бот Откачайка для водителей" \
            "Вы можете смотреть все заказы, выполнять их и тд" \
            "Все функции указаны на клавиатуре" \
            "Выберете из следующего списка команд:"
        await message.answer(text, reply_markup=main_menu_keyboard())

# @dp.message_handler(Text(equals=ORDERS, ignore_case=True))
# async def show_orders(message: Message):
#     if is_driver(message.chat.id):
#         orders = await get_orders(message.chat.id)
#         if orders:
#             for order in orders:
#                 await message.answer(get_order_info(order), reply_markup=inline_order_keyboard(order))
#         else:
#             await message.answer("На данный момент у вас нет заказов", reply_markup=not_available_orders_keyboard())


@dp.callback_query_handler(canceled_call_back.filter())
async def callback_canceled_order(call: CallbackQuery, callback_data: dict):
    order_id = callback_data['order_id']
    order = canceled_order(order_id)
    await call.message.edit_reply_markup(reply_markup=inline_order_keyboard(order))


@dp.callback_query_handler(in_progress_call_back.filter())
async def callback_started_order(call: CallbackQuery, callback_data: dict):
    order_id = callback_data['order_id']
    order = started_order(order_id)
    await call.message.edit_reply_markup(reply_markup=inline_order_keyboard(order))


@dp.callback_query_handler(completed_call_back.filter())
async def callback_completed_order(call: CallbackQuery, callback_data: dict):
    order_id = callback_data['order_id']
    order = completed_order(order_id)
    await call.message.edit_reply_markup(reply_markup=inline_order_keyboard(order))
