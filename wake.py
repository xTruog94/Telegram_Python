import telegram
import random
import requests
import time
import datetime
def send_message(messages):
    random_number = random.randint(0, 1000)
    telegram_notify = telegram.Bot("1203819953:AAFKQyXJp_MVoh4IB_Onw8Z14h334rZMB3c")
    telegram_notify.send_message(chat_id="1208424592", text=messages,
                            parse_mode='Markdown')
def send_message2(messages):
    random_number = random.randint(0, 1000)
    telegram_notify = telegram.Bot("1294069256:AAE8cTIOqTmah62hUBAZHihett8i2gtvFpI")
    telegram_notify.send_message(chat_id="-417251785", text=messages,
                            parse_mode='Markdown')
def current_weather():
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    city='Hanoi'
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Nhiệt độ trung bình là {temp} độ C
        Độ ẩm là {humidity}% \n """.format(day = now.day,month = now.month, year= now.year, temp = current_temperature, humidity = current_humidity)
        if 25<=current_temperature and current_temperature<=28:
            content=content+'Trời hôm nay khá mát mẻ đấy em \n Book một chú lịch đi chơi nào :))'
        elif 19<current_temperature<25:
            content=content+'Trời lạnh quá, phải mặc thêm áo thôi 😱😱'
        elif current_temperature>28:
            content=content+'Nóng quá, nóng quá, nóng quá đi'
        elif current_temperature<=19:
            content=content+'Hôm nay siêu siêu lạnh luôn đấy ! Mặc ấm vào em nhé.'
    return content
mess1=current_weather()
send_message(mess1)
mess2='Chúc bé có một ngày mới tràn đầy năng lượng 💪💪💪'
send_message(mess2)
send_message2(mess1)