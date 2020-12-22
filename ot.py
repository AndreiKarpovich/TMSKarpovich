import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, PrefixHandler

TOKEN = "1402311425:AAGIryuuT_cC5pop3Eu8RXvixWcEz_9IbU8"


def start(bot, context):
    bot.message.reply_text("Hello World!!!")



def math(bot, context):
    value = "".join(context.args)
    res = eval(value)
    bot.message.reply_text(str(res))

def savefile(bot, context):
    text = bot.message.text
    with open("text_file.txt", "w") as file:
        file.write(text)
    bot.message.reply_text("File Sozdan")
    

def getfile(bot, context):
    with open ("text_file.txt", "r") as file:
        t = file.read()
    bot.message.reply_text(str(t[:200]))
       

def addfile(bot, context):
    text = bot.message.text
    with open("text_file.txt", "a") as file:
        file.write(text)
    bot.message.reply_text("Tekst dobavlen")

def image(bot, context):
    im = context.bot.getFile(bot.message.photo[-1].file_id)
    im.download(bot.message.photo[-1].file_id + '.jpg')
    bot.message.reply_text("File sohranen")

def run():
    bot = Updater(TOKEN, use_context=True)
    bot.dispatcher.add_handler(CommandHandler("start", start))
    bot.dispatcher.add_handler(CommandHandler("math", math))
    bot.dispatcher.add_handler(CommandHandler("savefile", savefile))
    bot.dispatcher.add_handler(PrefixHandler('#', 'getfile', getfile))
    bot.dispatcher.add_handler(PrefixHandler('$', 'addfile', addfile))
    bot.dispatcher.add_handler(MessageHandler(Filters.photo, image))
    bot.start_polling()
    bot.idle()

if __name__ == "__main__":
    run()