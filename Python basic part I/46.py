# 46. Write a python program to get the path and name of the file that is currently executing.

import os
# return canonical path of file
print(os.path.realpath(__file__))
# return a relative path to file from current dir or from an optional start dir
try:
    print('relpath:', os.path.relpath(__file__, start='d:'))
except ValueError:
    print('Wrong path!')