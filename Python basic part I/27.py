# 27. Write a Python program to concatenate all elements in a list into a string and return it.

def concatenate_list(lst):
    #conv_lst = [str(l) for l in lst]
    return ''.join(conv_lst)

new_string = concatenate_list(['a', 'b', 1])
print(new_string)