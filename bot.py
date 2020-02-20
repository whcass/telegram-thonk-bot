from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import logging
import random
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
    print("Yeah we here yo")
    # context.bot.send_message(chat_id=update.effective_chat.id,text=update.message.text)
    if update.message.text.lower().startswith("i'm") or update.message.text.lower().startswith("im") or update.message.text.lower().startswith("i am"):
        reply_string = update.message.text.split(' ',1)[1]
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Hi {0}, I'm Dad! :)".format(reply_string),
            reply_to_message_id=update.message.message_id)
    elif "?" in update.message.text:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="🤔",
            reply_to_message_id=update.message.message_id
        )
    elif "🤔" in update.message.text:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="\"{0}\"\n\n Things that make you go hmmmmm 🤔".format(update.message.text)
            # reply_to_message_id=update.message.message_id
        )
    elif "xd" in update.message.text.lower():
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="\"{0}\"\n\n Epic gamer moment 😎".format(update.message.text)
        )
    elif ("fuck" in update.message.text.lower() or "shit" in update.message.text.lower()) and ("bot" in update.message.text.lower()):
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Hey, fuck you too!",
                reply_to_message_id=update.message.message_id
            ) 
    elif update.message.text.startswith("https://"):
        send_meme_image(update,context)
    else:
        rand = random.randint(1,20)
        if rand == 1:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="\"{0}\"\n\n Things that make you go hmmmmm 🤔".format(update.message.text)
                # reply_to_message_id=update.message.message_id
            )
        elif rand == 1:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="\"{0}\"\n\n Really makes you think doesn't it?".format(update.message.text)
                # reply_to_message_id=update.message.message_id
            )

def send_meme_image(update,context):
    rand = random.randint(1,5)
    if rand == 1 or True:
        randomimage = random.randint(1,2)
        image = 'images/clean.png'
        if randomimage == 1:
            image= 'images/deletethis.png'
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            reply_to_message_id=update.message.message_id,
            photo=open(image,'rb')
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