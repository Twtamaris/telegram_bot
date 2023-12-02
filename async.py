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


morning_subjects = ['OOAD', 'DBMS', 'DBMS', 'ES', 'ES', 'OOAD']
day_subjects = ['AI', 'ECONOMICS', 'ECONOMICS', 'OS', 'OS', 'AI']
dawn_subjects = ['Project Gr.D', 'Embeded System Lab', 'N', 'OOAD Lab', 'OS system lab', 'DBMS_Lab']
times = [current_time, "11:15", "13:30"]
subjects = [morning_subjects, day_subjects, dawn_subjects]


TOKEN = '6879758654:AAGqufutJfVU7Xtb-nXBmvxvgwCg4BoXcSI'
BOT_USERNAME = '@Saurabey_bot'
bot = telegram.Bot(token=TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am a banana!')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a banana! Please type something so I can respond!')

async def custom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

async def send_reminder():
    print('This is awesome')
    today = datetime.today().weekday()
    current_time =  datetime.now().strftime("%H:%M")
    print(current_time)
    if current_time in times:
        print('This is awesome')
        index_  = times.index(current_time)
        subject = subjects[index_][today]
        if subject != 'N':
            response =f"Hey! You have {subject} class in 15 minutes"
            print(response)
            await bot.send_message(chat_id='@Saurabey_bot', text=response)


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

    if chat_type == 'group' and BOT_USERNAME in user_text:
        response = handle_response(user_text.replace(BOT_USERNAME, '').strip())
    else:
        response = handle_response(user_text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        chat_id = update.channel_post.chat.id  # Access channel-specific chat ID
        print(f'Update [{update}] caused error ({context.error}) in channel {chat_id}')
    except AttributeError:
        print(f'An error occurred ({context.error}) in a non-channel context')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('custom', custom))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)
    asyncio.run(send_reminder())


    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)

