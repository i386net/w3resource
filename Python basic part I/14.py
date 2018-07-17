# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)

import datetime


def enter_date():
    date_dict = {}
    date_dict['year'] = int(input('Year: '))
    date_dict['month'] = int(input('Month: '))
    date_dict['day'] = int(input('Day: '))
    return date_dict

dd1 = enter_date()
dd2 = enter_date()

#print(datetime.date(**dd1)) # unpack dictionary keys
#print(datetime.date(**dd2))

# передача именованных аргументов из словаря и вычисление разницы по модулю
delta = abs(datetime.date(**dd2) - datetime.date(**dd1))
print('{} days'.format(delta.days))
