# 36. Write a Python program to add two objects if both objects are an integer type
import sys


def sumObjects(obj1, obj2):
    if type(obj1) == int and type(obj2) == int:
        return obj1 + obj2
    else:
        sys.exit()


print(sumObjects('a', 'b'))