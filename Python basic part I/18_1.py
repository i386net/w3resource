# 18. Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum
a,b,c = input('Enter 3 numbers: ').split(' ')

def calculate_sum(a,b,c):

    if int(a) == int(b) == int(c):
        return (int(a) + int(b) + int(c)) * 3
    else:
        return (int(a) + int(b) + int(c))

calculated_sum = calculate_sum(a, b, c)
print(calculated_sum)