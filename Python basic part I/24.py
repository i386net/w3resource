# 24. Write a Python program to test whether a passed letter is a vowel or not

def isVower(letter):
    vowels = 'aeuio'
    return letter in vowels

print(isVower('a'))
print(isVower('b'))