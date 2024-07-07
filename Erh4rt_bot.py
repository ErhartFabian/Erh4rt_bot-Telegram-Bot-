
import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import datetime
import threading

# Configurar el logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Lista de recordatorios
reminders = []

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hola! Soy tu bot personal. Usa el comando /remember seguido de la fecha y el mensaje.')

def remember(update: Update, context: CallbackContext) -> None:
    try:
        # Extract the date and the message from the user's input
        date_str = context.args[0]
        reminder_msg = ' '.join(context.args[1:])
        
        # Convert the date string to a datetime object
        reminder_date = datetime.datetime.strptime(date_str, '%d-%m-%Y')
        
        # Calculate the delay
        now = datetime.datetime.now()
        delay = (reminder_date - now).total_seconds()
        
        # Ensure the delay is positive
        if delay > 0:
            # Schedule the reminder
            threading.Timer(delay, send_reminder, [update.message.chat_id, reminder_msg, context]).start()
            update.message.reply_text(f'Recordatorio programado para {date_str}')
        else:
            update.message.reply_text('La fecha debe estar en el futuro.')
    except (IndexError, ValueError):
        update.message.reply_text('Uso: /remember <DD-MM-AAAA> <mensaje>')

def send_reminder(chat_id, message, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=chat_id, text=f'Hola soy tu bot personal y te recuerdo: {message}')

def main() -> None:
    # Token del bot de Telegram
    TOKEN = '7418504659:AAFuHhGGY3sXWGYeD3o9zIHul_3b3zq4t40'
    
    # Crear el updater y el dispatcher
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    # Añadir manejadores de comandos
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("remember", remember))

    # Empezar el bot
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
