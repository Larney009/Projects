from typing import Final
from telegram import Update
from Scrap.scrap import movies
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

Token: Final = '7111986900:AAFBQv8Q-egCKsCtJzPrtpylCavVLNCBja8'
Bot_Username: Final = '@MovieDoorBot'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Welcome to Movie List Bot!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Need help? Type what it is that you need assistance with!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Custom from Custard!')

async def january_movies_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Send the file content as a message
    message = movies
    await update.message.reply_text(text=message)
    
#Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how are you' in processed:
        return 'I am good'
    
    if 'i love python' in processed:
        return 'I love python too!'
    
    if 'movies released in january?' in processed:
        return 'Movies released in Jaunuary:'
    
    return 'I do not understand what you wrote...'

async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str =  update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}:"{text}"')

    if message_type == 'group':
        if Bot_Username in text:
            new_text: str = text.replace(Bot_Username, '').strip()
            response: str = handle_response(new_text)
        else:
            return 
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update{update} caused error {context.error}')



if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(Token).build()

    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('january_movies', january_movies_command))


    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))


    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)