# 27. Write a Python program to concatenate all elements in a list into a string and return it.

def concatenate_list(lst):
    #конвернтация элементов списка через генератор в строку
    return ''.join([str(l) for l in lst])

new_string = concatenate_list(['a', 'b', -1])
print(new_string)