from aiogram.types import Message, ReplyKeyboardRemove
from .keyboards import main_menu_keyboard
from config import dp


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    text = "Привет это бот Откачайка для водителей" \
        "Вы можете смотреть все заказы, выполнять их и тд" \
        "Все функции указаны на клавиатуре"
    await message.answer(text, reply_markup=main_menu_keyboard())
