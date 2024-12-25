from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

# Pegando o token do bot pela variável de ambiente
API_TOKEN = os.getenv('API_TOKEN')

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
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher

    # Configurando comandos e mensagens
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.all, echo))

    # Iniciando o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
