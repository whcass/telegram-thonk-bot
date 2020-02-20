from telegram.ext import Updater
from telegram.ext import CommandHandler
import json
import logging


def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Hurr durr I'm a bot lmao")

def main():
    # Load the secret from the secret.json file
    with open('secret.json') as f:
        data = json.load(f)

    secret = data['secret']
    
    # Setup our basic stuff
    updater = Updater(token=secret,use_context=True)
    dispatcher = updater.dispatcher
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
    
    # Setup our handlers 
    start_handler = CommandHandler('start',start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()

if __name__ == '__main__':
    main()