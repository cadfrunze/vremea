import requests
from datetime import datetime
import time

ALERT_VREMEA: list = [1006, 1009, 1063, 1087, 1180, 1183, 1186, 1189, 1192, 1195, 1237, 1240, 1243, 1246, 1249, 1252,
                      1273, 1276]

MY_API = '37f43c11b8f14ec799371509232907'
ora_actuala: int = datetime.now().hour
parametrii: dict = {
    'key': MY_API,
    'q': 'Regensburg',
    # 'hour': ora_actuala,
    'lang': 'ro'

}
ora_target = ''


def vremea():
    """Functie pt avertizare vreme rea!"""
    global ora_actuala, ora_target
    if ora_actuala == 9 or ora_actuala == 18:
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
                rezultat: list = date_json['forecast']['forecastday'][0]['hour'][ora_actuala:ora_actuala + 4]
                coduri_target: list = []
                for element in rezultat:
                    print(element['time'])
                    conditia_vremii = element['condition']['code']
                    if conditia_vremii in ALERT_VREMEA:
                        ora_vreme_rea = conditia_vremii['condition']['time']
                        print(ora_vreme_rea)
                        coduri_target.append(conditia_vremii)

                minut_sleep = 60 - datetime.now().minute
                # print(minut_sleep)
                print(f"Trebuie sa ateptam: {(minut_sleep + 1) * 60} secunde")
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
