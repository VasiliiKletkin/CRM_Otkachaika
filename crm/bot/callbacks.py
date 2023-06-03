import telebot
from telebot import AdvancedCustomFilter, types
from telebot.callback_data import CallbackData, CallbackDataFilter

order_callback = CallbackData('button', 'order_id', prefix='order')

class OrderCallbackFilter(AdvancedCustomFilter):
    key = 'order_config'

    def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)


def bind_filters(bot: telebot.TeleBot):
    bot.add_custom_filter(OrderCallbackFilter())
