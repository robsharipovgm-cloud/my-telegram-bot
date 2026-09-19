import telebot
import random
import os
import threading
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

bot_token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['yesno'])
def yes_no(message):
    answer = random.choice(['Да', 'Нет'])
    bot.reply_to(message, answer)

@bot.message_handler(func=lambda message: True)
def echo(message):
    hint = 'Напиши /yesno'
    bot.reply_to(message, hint)

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        text = 'Bot is running'
        data = text.encode()
        self.wfile.write(data)

def run_web_server():
    port_text = os.environ.get('PORT', '8080')
    port = int(port_text)
    host = '0.0.0.0'
    addr = host, port
    server = HTTPServer(addr, WebServer)
    server.serve_forever()

if __name__ == '__main__':
    bot.remove_webhook()
    t = threading.Thread(target=run_web_server)
    t.start()
    bot.infinity_polling()
