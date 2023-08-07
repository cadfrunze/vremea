import requests
from datetime import datetime

LON = 23.6
LAT = 46.7667
MY_API = '37f43c11b8f14ec799371509232907'
ora_actuala: int = datetime.now().hour
parametrii: dict = {
    'key': MY_API,
    'q': 'Cluj-Napoca',
    'hour': ora_actuala,
    'lang': 'ro'

}

while True:
    if ora_actuala == 5 or ora_actuala == 20:
        start_time = datetime.now()
        raspuns = requests.get(url='http://api.weatherapi.com/v1/forecast.json', params=parametrii)
        end_time = datetime.now()
        calculate_time = (f'Am raspuns in min: {int((end_time - start_time).total_seconds() // 60)}',
                          f'sec: {(end_time - start_time).total_seconds()}')
        print(calculate_time)
        raspuns.raise_for_status()
        date_json: dict = raspuns.json()
        print(date_json)
        rezultat: str = date_json['forecast']['forecastday'][0]['hour'][0]['condition']['code']
        print('Vremea de azi:', rezultat)
        break
