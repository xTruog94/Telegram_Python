import telegram
import random
import requests
import time
import datetime
list_quote=[]
with open('quotes.txt','r') as lines:
    for line in lines:
        list_quote.append(str(line).rstrip('\n'))
def send_message():
    random_number = random.randint(0, 99)
    telegram_notify = telegram.Bot("1203819953:AAFKQyXJp_MVoh4IB_Onw8Z14h334rZMB3c")
    messages=list_quote[random_number]
    telegram_notify.send_message(chat_id="1208424592", text=messages,
                            parse_mode='Markdown')
send_message()