from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from .keyboards import main_menu_keyboard, MAIN_MENU
from config import dp


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    text = "Привет это бот Откачайка для водителей" \
        "Вы можете смотреть все заказы, выполнять их и тд" \
        "Все функции указаны на клавиатуре"
    await message.answer(text, reply_markup=main_menu_keyboard())


@dp.message_handler(Text(equals=MAIN_MENU.ORDERS, ignore_case=True))
async def show_commands(message: Message):
    await message.answer("Выбирете из следующего списка команд:", reply_markup=keyboard)
    await OrderMessDriver.wait_choose_command.set()

