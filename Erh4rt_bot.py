import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.Telebot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message,"Hola!, como va todo?")

bot.polling()