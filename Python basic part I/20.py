# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

n = int(input('Enter number: '))
s = input('String: ')

multiply_sting = lambda s, n: s * n
print(multiply_sting(s, n))