# Write a Python program to print without newline or space

def line(l,r=10):
    if len(l) > 1:
        print('too long string')
    for i in range(r):
        print(l, end='')

s = input('String>>> ')
line(s)