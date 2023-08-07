import requests
from datetime import datetime
import time
# dsasdasd
ALERT_VREMEA: list = [1006, 1009, 1063, 1087, 1180, 1183, 1186, 1189, 1192, 1195, 1237, 1240, 1243, 1246, 1249, 1252,
                      1273, 1276]

MY_API = '37f43c11b8f14ec799371509232907'
ora_actuala: int = datetime.now().hour
parametrii: dict = {
    'key': MY_API,
    'q': 'Östersund',
    'hour': ora_actuala,
    'lang': 'ro'

}


def vremea():
    """Aleratere vreme rea!"""
    global ora_actuala
    if ora_actuala == 9 or ora_actuala == 0:
        while True:
            try:
                raspuns = requests.get(url='http://api.weatherapi.com/v1/forecast.json', params=parametrii)
                raspuns.raise_for_status()
            except requests.exceptions.ConnectTimeout:
                # Aici va continua la while loop
                continue
            else:
                # raspuns va primi valoarea de counexiune 200 si va prelua datele
                date_json: dict = raspuns.json()
                # print(date_json)
                rezultat: int = date_json['forecast']['forecastday'][0]['hour'][0]['condition']['code']
                print('Vremea de azi:', rezultat)
                minut_sleep = 60 - datetime.now().minute
                # print(minut_sleep)
                print(f"Trebuie sa ateptam: {(minut_sleep + 1) * 60} secunde")
                if rezultat in ALERT_VREMEA:
                    print('ubmrela')
                time.sleep(int((minut_sleep + 1) * 60))
                break
    ora_actuala = datetime.now().hour
    while ora_actuala != 9 and ora_actuala != 0:
        ora_actuala = datetime.now().hour
        print('am intrat in ora diferita')
        # Daca ora este diferita va continua pana la ora afisata conform cerintelor
        continue
    vremea()


vremea()
