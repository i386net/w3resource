# 36. Write a Python program to add two objects if both objects are an integer type

def sumObjects(obj1, obj2):
    if type(obj1) == int and type(obj2) == int:
        return obj1 + obj2
    else:
        return 'Must be integers'


print(sumObjects('a', 'b'))