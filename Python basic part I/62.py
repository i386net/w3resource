# 62. Write a Python program to convert all units of time into seconds

time_units = input('enter time units d,h,m,s: ').split()

time_units[0] = int(time_units[0]) * 86400
time_units[1] = int(time_units[1]) * 3600
time_units[2] = int(time_units[2]) * 60
time_units[-1] = int(time_units[-1])
print(sum(time_units))