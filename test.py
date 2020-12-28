import telegram
import random
import requests
import time
import datetime

def send_message(messages):
    random_number = random.randint(0, 1000)
    telegram_notify = telegram.Bot("1294069256:AAE8cTIOqTmah62hUBAZHihett8i2gtvFpI")
    telegram_notify.send_message(chat_id="-417251785", text=messages,
                            parse_mode='Markdown')
def current_weather():
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    city='Hà Nội'
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_humidity = city_res["humidity"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Nhiệt độ trung bình là {temp} độ C
        Độ ẩm là {humidity}%
        """.format(day = now.day,month = now.month, year= now.year, temp = current_temperature, humidity = current_humidity)
    return content
mess=current_weather()
send_message(mess)