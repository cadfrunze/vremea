import requests
from datetime import datetime
import time
from twilio.rest import Client

ALERT_VREMEA: list = [1006, 1009, 1063, 1087, 1180, 1183, 1186, 1189, 1192, 1195, 1237, 1240, 1243, 1246, 1249, 1252,
                      1273, 1276]

MY_API = 'test'
TWILIO_ACCOUNT_SID = 'test'
AUTH_TOKEN = 'test'
TWILIO_NUM = 'test'

parametrii: dict = {
    'key': MY_API,
    'q': 'Cluj-Napoca',
    'lang': 'ro'

}
client = Client(TWILIO_ACCOUNT_SID, AUTH_TOKEN)


if datetime.now().hour == 2:
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
            rezultat: list = date_json['forecast']['forecastday'][0]['hour'] \
                [datetime.now().hour + 3:datetime.now().hour + 4]
            coduri_target: dict = {}
            for element in rezultat:
                if element['condition']['code'] in ALERT_VREMEA:
                    new_element: str = element['time'].split(' ')[-1]
                    coduri_target[element['condition']['code']] = new_element
            if len(coduri_target) > 1:
                if len(coduri_target) > 1:
                    mesaj: str = 'Intre orele: ' + ','.join(coduri_target.values()) + ' trebuie sa iti iei umbrela!'
                    message = client.messages.create(to='+test', from_=TWILIO_NUM, body=mesaj)
                else:
                    mesaj: str = 'La ora ' + ','.join(coduri_target.values()) + ' trebuie sa iti iei umbrela!'
                    message = client.messages.create(to='+40743507250', from_=TWILIO_NUM, body=mesaj)
                coduri_target.clear()
            minut_sleep = 60 - datetime.now().minute
            time.sleep(int((minut_sleep + 1) * 60))
