import sys
import time
import random
import datetime
import telepot

def handle(msg):
    chat_id = msg['chat']['id']
    bot.sendMessage(chat_id, "Hello")
    bot = telepot.Bot('316622281:AAF1wQz7A1JVqlDEYbtz76VhXKrh0aCASqI')
    bot.message_loop(handle)    
    
    
