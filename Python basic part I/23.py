# 23. Write a Python program to get the n (non-negative integer) copies of
# the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2

def getString(n, string):
    if n < 0:
        print('Negative integers are not acceptable!')
    if len(string) < 2:
        return string * n
    else:
        return string[:2] * n

num = int(input('Enter any number: '))
s = input('String: ')

new_string = getString(num, s)
print(new_string)