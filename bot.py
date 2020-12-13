import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "1402311425:AAGIryuuT_cC5pop3Eu8RXvixWcEz_9IbU8"


def start(bot, context):
    bot.message.reply_text("Hello World!!!")


def message(bot, context):
    text = bot.message.text
    count = len(text)
    response = "В Вашем сообщении {} символов."
    bot.message.reply_text(response.format(count))

def math(bot, context):
    value = "".join(context.args)
    res = eval(value)
    bot.message.reply_text(str(res))


def run():
    bot = Updater(TOKEN, use_context=True)
    bot.dispatcher.add_handler(CommandHandler("start", start))
    bot.dispatcher.add_handler(CommandHandler("math", math))
    bot.dispatcher.add_handler(MessageHandler(Filters.text, message))
    bot.start_polling()
    bot.idle()

if __name__ == "__main__":
    run()