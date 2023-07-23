import requests


# lon = 23.58
# lat = 46.76
parametrii: dict = {
    'q': 'Cluj-Napoca',
    'appid': '****'
}
raspuns = requests.get(url='http://api.openweathermap.org/data/2.5/weather?', params=parametrii)
raspuns.raise_for_status()
date_json: dict = raspuns.json()
print(date_json)