from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = InlineKeyboardButton(text='7(800)555-35-35', url = 'tel:+78005553535'), InlineKeyboardButton(text='8(800)555-35-35', url = 'tel:+88005553535')

start_keyboard = ReplyKeyboardMarkup(resize_keyboard = True).add(inline_keyboard)