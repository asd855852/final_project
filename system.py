import datetime
import time
from PIL import Image, ImageTk

import api

settings = dict(
    # True: 12hour round, False: 24hour round
    AMPM=False,

    country='tw',
    #country='jp',
    # en:English, ja:Japanese
    lang='ja',
    #lang='tw-ch',
    #lang='tw',
    # To find your city available,search by here.
    #https://openweathermap.org/find
    #location='Taiwan, TW',
    location='Yokohama, JP',
    #location='New York City, US',
    name="keo",

    icon='./user/keo.jpg'
)
def nowTime():
    AMPM = settings.get("AMPM")
    dt_now = datetime.datetime.now()
    if (AMPM):
        if dt_now.hour < 12:
            s = 'AM{0:02d}:{1:02d}:{2:02d}'.format(dt_now.hour, dt_now.minute, dt_now.second)
        else:
            nowhour = dt_now.hour - 12
            s = 'PM{0:02d}:{1:02d}:{2:02d}'.format(nowhour, dt_now.minute, dt_now.second)
    else:
        s = '{0:02d}:{1:02d}:{2:02d}'.format(
            dt_now.hour, dt_now.minute, dt_now.second)
    return s
def nowDate():
    date = datetime.datetime.now()
    weekday = date.weekday()
    lang = settings.get("lang")
    if lang=='ja':
        dict_week = {0:'月', 1:'火', 2:'水', 3:'木', 4:'金', 5:'土', 6:'日'}
        weekJP = dict_week.get(weekday)
        w = '{0}曜日'.format(weekJP)

        s = '{0}月{1}日'.format(date.month, date.day)
    elif lang == 'tw-ch':
        dict_week = {0:'一', 1:'二', 2:'三', 3:'四', 4:'五', 5:'六', 6:'天'}
        weekJP = dict_week.get(weekday)
        w = '星期{0}'.format(weekJP)

        s = '{0}月{1}日'.format(date.month, date.day)
    elif lang == 'en':
        dict_week = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
        weekJP = dict_week.get(weekday)
        w = '{0}'.format(weekJP)

        s = '{0} / {1}'.format(date.month, date.day)

    return [s,w]
    
def weatherJP(weatherEn):
    dict_weather = {'Sun':'晴れ','Clouds':'曇り','Rain':'雨','Snow':'雪','Thunder':'雷'}
    weatherJP = dict_weather.get(weatherEn)
    if (weatherJP):
        return weatherJP
    else:
        return weatherEn

def weatherTW(weatherEn):
    dict_weather = {'Sun':'晴天','Clouds':'多雲','Rain':'雨天','Snow':'下雪','Thunder':'打雷'}
    weatherTW = dict_weather.get(weatherEn)
    if (weatherTW):
        return weatherTW
    else:
        return weatherEn

def weatherUS(weatherEn):
    dict_weather = {'Sun':'Sunny','Clouds':'Clouds','Rain':'Rain','Snow':'Snow','Thunder':'Thunder'}
    weatherUS = dict_weather.get(weatherEn)
    if (weatherUS):
        return weatherUS
    else:
        return weatherEn

def getWeather():
    location = settings.get("location")
    lang = settings.get("lang")
    data = api.getWeather(location)
    weather_main = data.get('weather')[0].get('main')
    if lang == 'ja':
        weather_main = weatherJP(weather_main)
    if lang == 'tw-ch':
        weather_main = weatherTW(weather_main)
    if lang == 'en':
        weather_main = weatherUS(weather_main)

    temp = f'{data.get("main").get("temp")}°'
    location = data.get('name')
    icon_file = data.get('weather')[0].get('icon')
    icon_file = icon_file[:2]
    if icon_file == '04':
        icon_file = '03'
    if icon_file == '10':
        icon_file = '09'
    image = Image.open(f"icon.png")
    print(image)
    image = image.resize((100, 100), Image.ANTIALIAS)
    image = image.convert('RGB')
    photo = ImageTk.PhotoImage(image)

    return [weather_main,temp,photo,location]
