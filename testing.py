from datetime import datetime as dt
import time

minut = dt.now().minute
ora = dt.now().hour
ziua = dt.now().day
luna = dt.now().month
anul = dt.now().year

with open('./work_log.txt', 'a') as fisier:
    fisier.writelines(f'\nData: {ziua}/{luna}/{anul} | Ora:{ora}:{minut}')


# start_time = dt.now()
# time.sleep(4)
# end_time = dt.now()
#
# calculate_time = (
#     f'min: {int((end_time - start_time).total_seconds() // 60)}', f'sec: {(end_time - start_time).total_seconds()}')
# print(calculate_time)
