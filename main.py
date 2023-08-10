import requests
from datetime import datetime
import time

ALERT_VREMEA: list = [1006, 1009, 1063, 1087, 1180, 1183, 1186, 1189, 1192, 1195, 1237, 1240, 1243, 1246, 1249, 1252,
                      1273, 1276]

MY_API = '37f43c11b8f14ec799371509232907'

parametrii: dict = {
    'key': MY_API,
    'q': 'Veliki Preslav',
    # 'hour': ora_actuala,
    'lang': 'ro'

}


while True:
    if datetime.now().hour == 9 or datetime.now().hour == 21:
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
                rezultat: list = date_json['forecast']['forecastday'][0]['hour'][datetime.now().hour:datetime.now().hour+4]
                coduri_target: dict = {}
                for element in rezultat:
                    if element['condition']['code'] in ALERT_VREMEA:
                        new_element: str = element['time'].split(' ')[-1]
                        coduri_target[element['condition']['code']] = new_element
                if len(coduri_target) > 1:
                    if len(coduri_target) > 1:
                        mesaj: str = 'Intre orele: ' + ','.join(coduri_target.values()) + ' trebuie sa iti iei umbrela!'
                        print(mesaj)
                    else:
                        mesaj: str = 'La ora ' + ','.join(coduri_target.values()) + ' trebuie sa iti iei umbrela!'
                        print(mesaj)
                    coduri_target.clear()
                minut_sleep = 60 - datetime.now().minute
                # print(minut_sleep)
                print(f"Trebuie sa ateptam: {(minut_sleep + 1) * 60} secunde")
                time.sleep(int((minut_sleep + 1) * 60))
    while datetime.now().hour != 9 and datetime.now().hour != 0:
        print('am intrat in ora diferita')
        # Daca ora este diferita va continua pana la ora afisata conform cerintelor
        continue
