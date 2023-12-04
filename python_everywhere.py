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
from pytz import timezone

local_tz = timezone('Asia/Kathmandu')

current_time = datetime.now().strftime("%H:%M")


morning_subjects = ['OOAD', 'ES', 'DBMS', 'ES', 'DBMS','N', 'OOAD']
day_subjects = ['AI', 'ECONOMICS', 'ECONOMICS', 'AI', 'OS','N', 'OS']
dawn_subjects = ['DBMS Lab', 'Embedded System Lab', 'AI lab','N', 'OS Lab', 'N','DBMS']
times = ['09:46', "11:15", "13:30"]
subjects = [morning_subjects, day_subjects, dawn_subjects]

TOKEN = '6879758654:AAGqufutJfVU7Xtb-nXBmvxvgwCg4BoXcSI'
BOT_USERNAME = '@Saurabey_bot'
bot = telegram.Bot(token=TOKEN)

def get_local_time():
    # Get the current time in your local timezone
    local_time = datetime.now(local_tz)
    return local_time.strftime("%H:%M")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am a Saurabey!')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a Saurabey! Please type something so I can respond!')

async def custom(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

async def send_reminder():
    while True:
        print('Checking for classes...')
        today = datetime.today().weekday()
        current_time = get_local_time() 
        print(current_time)
        if current_time in times:
            print('Time matched')
            index_ = times.index(current_time)
            subject = subjects[index_][today]
            if subject != 'N':
                response = f"Hey! You have {subject} class in 15 minutes"
                print(response)
                await bot.send_message(chat_id='-4024365137', text=response)
        await asyncio.sleep(60)  # Sleep for 60 seconds (1 minute) before the next check



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


async def main():
    bot = telegram.Bot(token=TOKEN)
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)

    while True:
        try:
            # Check for classes and send reminders
            await send_reminder()
            await asyncio.sleep(60)  # Check every minute
        except Exception as e:
            print(f"Error occurred: {e}")
            await asyncio.sleep(10)  # Wait before retrying in case of an error

if __name__ == '__main__':
    print('Starting bot...')
    asyncio.run(main())