# Самостоятельная работа 1: все параметры datetime.now()
import datetime

x = datetime.datetime.now()
print(x.year, x.month, x.day, x.hour, x.minute, x.second)

# Самостоятельная работа 2: переименование функции date при импорте
from datetime import date as my_date

birthday = my_date(2017, 6, 1)
print(birthday)
