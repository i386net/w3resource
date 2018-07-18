# 19
#Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

def string_is(str):
    if len(str) > 0 and str[0:2] == 'Is':
        return str
    else:
        return 'Is' + str


s1 = input('String: ')
test_s = string_is(s1)
print(test_s)
