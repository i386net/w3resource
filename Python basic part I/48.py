# 48. Write a Python program to parse a string to Float or Integer.
s = ''
def parse_string(s):
    return (float(s), int(float(s)))

for n in parse_string('3434.44'):
    print(n)