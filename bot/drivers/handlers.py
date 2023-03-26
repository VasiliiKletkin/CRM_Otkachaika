from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from config import bot, dp
from drivers.api import canceled_order, completed_order, inprogress_order
from utils import get_order_info, get_orders_today, is_driver

from .callbacks import order_call_back
from .keyboards import inline_order_keyboard, main_menu_keyboard


@dp.message_handler(commands=['start', 'help'])
async def start(message: Message):
    if is_driver(message.chat.id):
        text = "Привет это бот Откачайка для водителей \n" \
            "Вам будут отправлять заказы в этот чат" \
            "Вы сможете их начать, завершить или отменить"
        await message.answer(text)


@dp.callback_query_handler(order_call_back.filter(status="CANCELED"))
async def callback_canceled_order(call: CallbackQuery, callback_data: dict):
    order = await canceled_order(callback_data['order_id'])
    await call.message.edit_reply_markup(reply_markup=inline_order_keyboard(order))


@dp.callback_query_handler(order_call_back.filter(status="INPROGRESS"))
async def callback_started_order(call: CallbackQuery, callback_data: dict):
    order = await inprogress_order(callback_data['order_id'])
    await call.message.edit_reply_markup(reply_markup=inline_order_keyboard(order))


@dp.callback_query_handler(order_call_back.filter(status="COMPLETED"))
async def callback_completed_order(call: CallbackQuery, callback_data: dict):
    order = await completed_order(callback_data['order_id'])
    await call.message.edit_reply_markup(reply_markup=inline_order_keyboard(order))


async def send_orders():
    for order in await get_orders_today():
        await bot.send_message(order["driver"]["profile"]["telegram_id"], get_order_info(order), reply_markup=inline_order_keyboard(order))
