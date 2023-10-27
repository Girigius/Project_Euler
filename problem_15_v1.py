"""
__author__ = "Girigius"
__version__ = "1"
__problem__ = "15"

Output:

"""


import time


def paths(m, n):
    if m == 0 or n == 0:
        return 1
    return paths(m-1, n) + paths(m, n-1)


def solution():
    return paths(20, 20)


time.ctime(0)
start_time = time.time()
x = solution()
end_time = time.time()
print(x)
print("Execution time:", end_time - start_time)

