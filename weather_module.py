import requests

def get_weather():
    weather = requests.get("http://api.openweathermap.org/data/2.5/find?q=Moscow,RU&type=like&units=metric&lang=ru&APPID=9e4de933f7597c192e48354e34f7115c")
    data = weather.json()
    avg_temp = data['list'][0]['main']['temp']
    max_temp = data['list'][0]['main']['temp_max']
    min_temp = data['list'][0]['main']['temp_min']
    desc = data['list'][0]["weather"][0]['description']
    rain = data['list'][0]['rain']
    wind = data['list'][0]['wind']['speed']
    weather_final = "Итак погода в Москве сегодня: " + '\n' + "В данный момент температура: " + str(avg_temp) + " градусов" + '\n' + "Максимальная температура: " + str(max_temp) + " градусов" + '\n' +"Минимальная температура: "   + str(min_temp) +  " градусов" + '\n' +"Описание: " + str(desc) + '\n' + "Дождь: " + str(rain) + '\n' + "Скорость ветра : " + str(wind)
    return weather_final