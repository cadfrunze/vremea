from datetime import datetime as dt

minut = dt.now().minute
ora = dt.now().hour
ziua = dt.now().day
luna = dt.now().month
anul = dt.now().year

with open('./work_log.txt', 'a') as fisier:
    fisier.writelines(f'Data: {ziua}/{luna}/{anul} | Ora:{ora}:{minut}')
