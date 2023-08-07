from datetime import datetime
import time

ora = datetime.now().hour
minut = datetime.now().minute


def teste():
    while ora != 20 or minut != 47:
        continue
    else:
        time.sleep(65)
        teste()


teste()
