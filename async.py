from typing import Final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import telegram
from datetime import datetime
import asyncio

current_time = datetime.now().strftime("%H:%M")

morning_subjects = ['OOAD', 'DBMS', 'DBMS', 'ES', 'ES','N', 'OOAD']
day_subjects = ['AI', 'ECONOMICS', 'ECONOMICS', 'OS', 'OS','N', 'AI']
dawn_subjects = ['Project Gr.D', 'Embedded System Lab', 'N', 'OOAD Lab', 'OS System Lab','N', 'DBMS_Lab']
times = ['09:46', "11:15", "13:30"]
subjects = [morning_subjects, day_subjects, dawn_subjects]

TOKEN = '6879758654:AAGqufutJfVU7Xtb-nXBmvxvgwCg4BoXcSI'
BOT_USERNAME = '@Saurabey_bot'
bot = telegram.Bot(token=TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am a Saurabey!')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a Saurabey! Please type something so I can respond!')

async def custom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

async def send_reminder():
    print('This is awesome')
    today = datetime.today().weekday()
    current_time = datetime.now().strftime("%H:%M")
    print(current_time)
    if current_time in times:
        print('Time matched')
        index_ = times.index(current_time)
        subject = subjects[index_][today]
        if subject != 'N':
            response = f"Hey! You have {subject} class in 15 minutes"
            print(response)
            await bot.send_message(chat_id='-4024365137', text=response)


def handle_response(text: str):
    processed_text = text.lower()
    if 'hello' in processed_text:
        return 'Hey there!'
    if 'how are you' in processed_text:
        return 'I am good!'
    if 'i love python' in processed_text:
        return 'Remember to subscribe!'
    return 'I do not understand what you wrote...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_type = update.message.chat.type
    user_text = update.message.text.lower()
    print(f'User ({update.message.chat.id}) in [{chat_type}]: "{user_text}"')

    if chat_type == 'group' or chat_type == 'supergroup':
        if BOT_USERNAME.lower() in user_text:
            response = handle_response(user_text.replace(BOT_USERNAME.lower(), '').strip())
        else:
            response = handle_response(user_text)
    else:
        response = handle_response(user_text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.channel_post:
            chat_id = update.channel_post.chat.id
            print(f'Update [{update}] caused error ({context.error}) in channel {chat_id}')
        else:
            print(f'Update [{update}] caused error ({context.error}) but is not a channel_post')
    except AttributeError:
        print(f'An error occurred ({context.error}) in a non-channel context')


if __name__ == '__main__':
    print('Starting bot...')
    loop = asyncio.get_event_loop()
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start))
    # Add other command handlers here...

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    # Add other message handlers here...

    # Errors
    app.add_error_handler(error)

    # Schedule the periodic reminder task
    loop.create_task(send_reminder())

    # Polls the bot
    print('Polling...')
    try:
        loop.run_until_complete(app.run_polling(poll_interval=3))
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(app.session.close())
