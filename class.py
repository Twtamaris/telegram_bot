from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

TOKEN = '6879758654:AAGqufutJfVU7Xtb-nXBmvxvgwCg4BoXcSI'

def start(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! Type /hello to get a greeting.")

def hello(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello there! Welcome to the bot!")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('hello', hello))

    application.run_polling()

if __name__ == '__main__':
    main()
