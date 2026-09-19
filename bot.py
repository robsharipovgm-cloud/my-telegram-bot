import os
import telebot
import random

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

@bot.message_handler(commands=['yesno'])
def yes_no(message):
    bot.reply_to(message, random.choice(["Да", "Нет"]))

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Напиши /yesno")
bot.remove_webhook()
bot.infinity_polling()