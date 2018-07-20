# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import sys
import platform

print('{} {}'.format(sys.maxsize, sys.maxsize > 2 ** 60))

print(platform.architecture())
