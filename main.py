import asyncio
import json

import aiohttp
import telegram
from telegram import Update
from telegram.ext import Filters, Updater, CommandHandler, MessageHandler, CallbackContext
import telebot
from aiohttp import web

API_TOKEN = '1797610577:AAGreUvnFnK1dfD5R3l1G0Bbr1FSd0JvNSU'

API_URL = 'https://api.telegram.org/bot%s/%s'

# app = web.Application(loop=loop, middlewares=[])
# app.router.add_post('/api/v1', handler)
# return app

# app = loop.run_until_comlete(init_app(loop))
# bot = telebot.TeleBot(API_TOKEN)
#
# web.run_app(app, host='0.0.0.0', port=4242)
# bot = Updater('1797610577:AAGreUvnFnK1dfD5R3l1G0Bbr1FSd0JvNSU')
# updater.start_webhook(listen='0.0.0.0',
#                       port=8443,
#                       url_path=API_TOKEN,
#                       key='private.key',
#                       cert='cert.pem',
#                       webhook_url='https://example.com:8443/%s' % API_TOKEN)
#
# dispatcher = bot.dispatcher
bot = telebot.TeleBot(API_TOKEN)

# def	start(bot: Update, context: CallbackContext) -> None:
# 	bot.message.reply_text(f'Доброго времени суток, {bot.effective_user.first_name}')
#
# def echo(bot: Updater, context: CallbackContext):
# 	bot.message.reply_text("lol")
#
# dispatcher.add_handler(CommandHandler('start', start))
# echo_handler = MessageHandler(Filters.text, echo)
# dispatcher.add_handler(echo_handler)
#
# def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
#     menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
#     if header_buttons:
#         menu.insert(0, header_buttons)
#     if footer_buttons:
#         menu.append(footer_buttons)
#     return menu

# @bot.message_handler(сontent_types='text')
# list_time = ['Сегодня', 'Завтра', 'Определенная дата']
# button_list = []
# for each in list_time:
#     button_list.append(InlineKeyboardButton(each, callback_data=each))


keyboard = [['Сегодня', 'Завтра'],
            ['Определенная дата']]
# @bot.message_handler(commands = ['start', 'help'])
markup = telegram.ReplyKeyboardMarkup(keyboard)
@bot.message_handler(content_types=['text'])
def	send_welcome(message):
    print(message)
    if message.text.lower() == '/start':
        bot.send_message(message.from_user.id, f'Здравствуйте, {message.from_user.first_name}. Когда хотите посетить мероприятие?', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'idk')


bot.polling(none_stop=True)