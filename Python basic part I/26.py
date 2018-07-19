# 26. Write a Python program to create a histogram from a given list of integers

def drawHistogram(lst):
    for num in lst:
        print('🔴' * num)

drawHistogram([4, 5, 1, 2, 6, 9])