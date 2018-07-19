# 22. Write a Python program to count the number 4 in a given list.

def counter(lst):
    return lst.count(4)


l = [4, 1 ,2 , 4, 6 , 5]
c = counter(l)
print(c)