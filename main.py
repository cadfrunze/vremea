import requests
from datetime import datetime
import time

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


def vremea():
    """Aleratere vreme rea!"""
    if ora_actuala == 21:
        while True:
            try:
                raspuns = requests.get(url='http://api.weatherapi.com/v1/forecast.json', params=parametrii)
                raspuns.raise_for_status()
            except requests.exceptions.ConnectTimeout:
                print('am intrat in exceptie')
                continue
            else:
                print('am intrat in else_try')
                date_json: dict = raspuns.json()
                print(date_json)
                rezultat: int = date_json['forecast']['forecastday'][0]['hour'][0]['condition']['code']
                print('Vremea de azi:', rezultat)
                time.sleep(3600)
                break

    else:
        while ora_actuala != 21:
            continue
        else:
            vremea()


vremea()
