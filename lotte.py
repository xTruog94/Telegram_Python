import requests
from bs4 import BeautifulSoup
import re
import telegram
import datetime
def xskt():
    x = requests.get('https://xskt.com.vn/')
    soup = BeautifulSoup(x.content, "html.parser")
    titles = soup.findAll(class_='result',id="MB0")
    result = [tmp.find('em') for tmp in titles]
    pattern='[0-9]{5}'
    res=re.search(pattern,str(result)).group()
    return res
def send_message(messages):
    telegram_notify = telegram.Bot("1294069256:AAE8cTIOqTmah62hUBAZHihett8i2gtvFpI")
    telegram_notify.send_message(chat_id="-417251785", text=messages,
                            parse_mode='Markdown')
now = datetime.datetime.now()
mess= ''' Kết quả ngày {day} tháng {month} là '''.format(day=now.day,month=now.month)
mess=mess+xskt()
send_message(mess)