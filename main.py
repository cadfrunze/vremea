import requests
from datetime import datetime


LON = 23.6
LAT = 46.7667
MY_API = '**'
parametrii: dict = {
    'lat': LAT,
    'lon': LON,
    'appid': MY_API,
    'lang': 'ro',
    'units': 'metric'
}

while True:
    if datetime.now().hour == 22:
        raspuns = requests.get(url='https://api.openweathermap.org/data/2.5/weather', params=parametrii)
        raspuns.raise_for_status()
        date_json: dict = raspuns.json()
        print(date_json)
        break
