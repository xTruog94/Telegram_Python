import telegram
mess='Uống nước để có một làn da đẹp thôi nào 🥛🥛'
def send_message(messages):
    telegram_notify = telegram.Bot("1203819953:AAFKQyXJp_MVoh4IB_Onw8Z14h334rZMB3c")
    telegram_notify.send_message(chat_id="1208424592", text=messages,
                            parse_mode='Markdown')
send_message(mess)