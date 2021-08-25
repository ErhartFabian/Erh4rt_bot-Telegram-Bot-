import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot("API_KEY", parse_mode=None)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message,"Hola!, como va todo?")

bot.polling()