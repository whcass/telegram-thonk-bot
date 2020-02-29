#!/usr/bin/python3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import logging
import random
import os
import re

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Hurr durr I'm a bot lmao")

def thonk(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="""⠀      ⠰⡿⠿⠛⠛⠻⠿⣷
⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀
⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷
⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀ ⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠈⠉⠁

⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀
⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗
⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄
⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁
⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟
⠀⠀⠀⠀⠀⠉⠉⠉
""")

def memes(update,context):
    possesives = ["im", "i'm", "i am"]
    # context.bot.send_message(chat_id=update.effective_chat.id,text=update.message.text)
    text = update.message.text
    if update.effective_user.id == 854734710:
        return None
    elif text.startswith(tuple(possesives)) and len(text) < 20:
        reply_string = text
        for p in possesives:
            reply_string = re.sub(p, "", text)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text = "Hi {reply_string}, I'm Dad! :)",
            reply_to_message_id=update.message.message_id)
    elif "?" in text:
        rand = random.randint(1,100)
        if rand == 1:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="\"{text}\"\n\n Things that make you go hmmmmm 🤔",
                reply_to_message_id=update.message.message_id
            )
    elif "🤔" in text:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="🤔",
            reply_to_message_id=update.message.message_id
        )
    elif "xd" in text.lower():
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="\"{text}\"\n\n Epic gamer moment 😎"
        )
    elif ("fuck" in text.lower() or "shit" in text.lower()) and ("bot" in text.lower() or "thonk" in text.lower()):
        with open('insults.json') as f:
            data = json.load(f)
        
        insults = data['insults']
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=random.choice(insults),
            reply_to_message_id=update.message.message_id
        ) 
    elif ("thanks" in text.lower() and ("bot" in text.lower() or "thonk" in text.lower())):
        context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="You're welcome!",
                reply_to_message_id=update.message.message_id
            ) 
    elif text.startswith("https://"):
        send_meme_image(update,context)
    # else:
    #     rand = random.randint(1,100)
    #     if rand == 1:
    #         context.bot.send_message(
    #             chat_id=update.effective_chat.id,
    #             text="\"{0}\"\n\n Things that make you go hmmmmm 🤔".format(update.message.text)
    #             # reply_to_message_id=update.message.message_id
    #         )
    #     elif rand == 2:
    #         context.bot.send_message(
    #             chat_id=update.effective_chat.id,
    #             text="\"{0}\"\n\n Really makes you think doesn't it?".format(update.message.text)
    #             # reply_to_message_id=update.message.message_id
    #         )

def send_meme_image(update,context):
    rand = random.randint(1,50)
    if rand == 1:
        random_file = random.choice(os.listdir("images"))
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            reply_to_message_id=update.message.message_id,
            photo=open('images/'+random_file,'rb')
        )


def error(update,context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Load the secret from the secret.json file
    with open('secret.json') as f:
        data = json.load(f)

    secret = data['secret']
    
    # Setup our basic stuff
    updater = Updater(token=secret,use_context=True)
    dispatcher = updater.dispatcher

    
    # Setup our handlers 
    start_handler = CommandHandler('start',start)
    dispatcher.add_handler(start_handler)
    thonk_handler = CommandHandler('thonk',thonk)
    dispatcher.add_handler(thonk_handler)
    dispatcher.add_handler(MessageHandler(Filters.text,memes))
    dispatcher.add_handler(MessageHandler(Filters.photo,send_meme_image))
    updater.start_polling()

if __name__ == '__main__':
    main()