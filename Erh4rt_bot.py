import os
import telebot

#API_KEY = os.getenv('API_KEY') // ARREGLAR
bot = telebot.TeleBot('1942968058:AAE9dqYzQqnUw_ctwZUjRDS8YeQTOL3zHh4')

#Mensaje de bienvenida comandos Start y Greet
@bot.message_handler(commands=['Start','Greet'])
def greet(message):
    bot.reply_to(message,"Hola!, como va todo?")

#Mensaje ante cualquier comando no valido o texto
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.send_message(message.chat.id, 'Introduce un comando valido')



bot.polling() #Buscando entrada de mensajes
