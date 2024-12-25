from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from flask import Flask
import os

# Configurações do Telegram
API_TOKEN = os.getenv('API_TOKEN')

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá! Estou ativo e pronto para responder!')

def echo(update: Update, context: CallbackContext) -> None:
    if update.message.text:
        update.message.reply_text(update.message.text)
    elif update.message.photo:
        update.message.reply_photo(update.message.photo[-1].file_id)
    elif update.message.video:
        update.message.reply_video(update.message.video.file_id)
    elif update.message.sticker:
        update.message.reply_sticker(update.message.sticker.file_id)
    else:
        update.message.reply_text("Recebi algo que não sei como lidar!")

def main():
    # Start the bot on a separate thread
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.all, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    from threading import Thread

    # Run Flask server on port 5000 (render expects an open port)
    def run():
        app.run(host='0.0.0.0', port=5000)

    thread = Thread(target=run)
    thread.start()

    # Start bot
    main()
