# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)

import datetime

#c1 = datetime.date(2018, 7, 1)
#c2 = datetime.date(2018, 7, 10)
#print(c2-c1)

#date1 = {}
#date2 = {}

def enter_date():
    date_dict = {}
    date_dict['year'] = int(input('Year: '))
    date_dict['month'] = int(input('Month: '))
    date_dict['day'] = int(input('Day: '))
    return date_dict

dd1 = enter_date()
dd2 = enter_date()

print(datetime.date(**dd1))
print(datetime.date(**dd2))
delta = abs(datetime.date(**dd2) - datetime.date(**dd1))
print('{} days'.format(delta.days))
