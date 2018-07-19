# 38. Write a Python program to solve (x + y) * (x + y)


def solve(x,y):
    result = (x + y)**2
    return '({} + {})^2 = {}'.format(x, y, result)


print(solve(4, 3))
print(solve(3, 3))
print(solve(6, 4))
