from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from config import dp, bot
from datetime import datetime


@dp.message_handler(commands="cancel", state="*")
@dp.message_handler(Text(equals="отмена", ignore_case=True), state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):
    # Сбрасываем текущее состояние пользователя и сохранённые о нём данные
    await state.finish()
    await message.answer("Действие отменено", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=["start"], state="*")
@dp.message_handler(Text(equals="старт", ignore_case=True), state="*")
async def cmd_start(message: types.Message, state: FSMContext):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("МЕНЮ"))
    await message.answer("👋 Приветсвую Вас, " + str(message.from_user.full_name) + "\n"
                         "Я бот ОТКАЧАЙКА приму любые ваши пожелания и сделаю все неообходимое, чтобы откачать вашу яму ),"
                         "Нажмите ниже на МЕНЮ, чтобы посмотреть ваши возможности.", reply_markup=keyboard)
