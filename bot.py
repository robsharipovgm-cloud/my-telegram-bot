import <'telebot'>
import random
import os
import threading
from 'http.server'
import BaseHTTPRequestHandler, HTTPServer bot ='telebot'.TeleBot(os.environ.get ('BOT_TOKEN')) @bot.message_handler(commands= ['yesno'])
def yes_no(message): bot.reply_to (message, random.choice(["Да", "Нет"]))@bot.message_handler(func = lambda message: True)
def echo (message):bot.reply_to(message,"Напиши /yesno")
class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")
def run_web_server():
    port = int(os.environ.get('PORT', 8080))
        server = HTTPServer(('0.0.0.0', port), WebServer)
        server.serve_forever()
if __name__ = "__main__":
    bot.remove_webhook()
    threading.Thread(target=run_web_server).start()
    bot.infinity_polling()
