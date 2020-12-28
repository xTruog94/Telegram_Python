import telegram
import requests
import time
import datetime
def send_message(messages):
    telegram_notify = telegram.Bot("1203819953:AAFKQyXJp_MVoh4IB_Onw8Z14h334rZMB3c")
    telegram_notify.send_message(chat_id="1208424592", text=messages,
                            parse_mode='Markdown')
mess1='Chúc bé chang ngủ ngon 😴😴'
mess2='Anh yêu em nhiềuuuuuuuuuu ❤️💛💚💙💜🖤'
send_message(mess1)
send_message(mess2)
#1294069256:AAE8cTIOqTmah62hUBAZHihett8i2gtvFpI
#1203819953:AAFKQyXJp_MVoh4IB_Onw8Z14h334rZMB3c
#1208424592