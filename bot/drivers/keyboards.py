from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

ORDERS = 'ЗАКАЗЫ'
MAIN_MENU = (
    (ORDERS, "orders" ),
)

def main_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(row_width=1)
    for button in MAIN_MENU:
        keyboard.add(KeyboardButton(ORDERS))
    return keyboard
