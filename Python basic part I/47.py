# 47. Write a Python program to find out the number of CPUs using

import os
import multiprocessing
print('CPUs: {}'.format(os.cpu_count()))
print(multiprocessing.cpu_count())