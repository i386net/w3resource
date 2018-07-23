# 128. Write a Python program to check if lowercase letters exist in a string
str1 = '134431FFFF1'


def is_lower(string):
    for letter in string:
        if letter.islower():
            return True
    return False

def if_lower(string):
    # any -> return True if any element of iterable is true.
    return any(l.islower() for l in string)

print(is_lower(str1))
print(if_lower(str1))
