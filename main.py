from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


bot = Updater('1797610577:AAGreUvnFnK1dfD5R3l1G0Bbr1FSd0JvNSU')

def	start(bot: Update, context: CallbackContext) -> None:
	bot.message.reply_text(f'Доброго времени суток, {bot.effective_user.first_name}')

bot.dispatcher.add_handler(CommandHandler('start', start))


#@bot.message_handler(commands = ['start', 'help'])
# @bot.message_handler(сontent_types = ['start', 'help'])
#def	send_welcome(message):
#	bot.send_message(message, f'Доброго времени суток. {message.from_user.first_name}')

bot.start_polling()