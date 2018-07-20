# 45. Write a python program to call an external command in Python

import os
import subprocess

print('working dir: {}'.format(os.getcwd()))
print('User: {}'.format(os.getlogin()))
print(os.listdir('.'))
for i in os.scandir(path='/Users/'):
    print(i)

print(subprocess.run(['ps', 'aux']))