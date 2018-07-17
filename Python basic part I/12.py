# 12. Write a Python program to print the calendar of a given month and year.

import calendar

help(calendar)

m = int(input('Month: '))
y = int(input('Year: '))
print(calendar.month(y, m))
print(calendar.monthrange(y, m))
print(calendar.monthcalendar(y, m))