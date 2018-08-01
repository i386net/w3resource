
import pstats
import cProfile

def f():
    s = 0
    for i in range(100000):
        s += i
    print(s)

cProfile.run(f())