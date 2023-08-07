# import pandas
# from pathlib import Path
#
# date_lista_cod: list = []
# date_lista_str: list = []
# while True:
#     date_cod: int = int(input('zii codul: '))
#     date_str: str = input('zii strul: ')
#     if date_cod == 0 or date_str == 'code70':
#         break
#     date_lista_cod.append(date_cod)
#     date_lista_str.append(date_str)
#
# date_dict = {
#     'codul': date_lista_cod,
#     'vremea': date_lista_str
# }
#
# date_csv = pandas.DataFrame(data=date_dict)
#
# file_path = Path('./date/date.csv')
# date_csv.to_csv(file_path, index=False)
