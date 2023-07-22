import requests


lon = 23.58
lat = 46.76
parametrii: dict = {
    'q': 'Cluj-Napoca',
    'ro&APPID': 'doar nu sunt bou sa ti-l arat!'
}
raspuns = requests.get(url='api.openweathermap.org/data/2.5/weather?', params=parametrii)
raspuns.raise_for_status()
date_json: dict = raspuns.json()
print(date_json)