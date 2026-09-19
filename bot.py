import telebot
import random
import os
import threading
from http.server import (
    BaseHTTPRequestHandler,
    HTTPServer,
)

bot = telebot.TeleBot(
    os.environ.get('BOT_TOKEN')
)

@bot.message_handler(commands=['yesno'])
def yes_no(message):
    answer = random.choice(["Да", "Нет"])
    bot.reply_to(message, answer)

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "Напиши /yesno")

class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        msg = b"Bot is running"
        self.wfile.write(msg)

def run_web_server():
    port_str = os.environ.get('PORT', 8080)
    port = int(port_str)
    addr = ('0.0.0.0
', port)
    server = HTTPServer(addr, WebServer)
    server.serve_forever()

if __name__ == "__main__":
    bot.remove_webhook()
    t = threading.Thread(target=run_web_server)
    t.start()
    bot.infinity_polling()
