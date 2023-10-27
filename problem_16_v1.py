"""
__author__ = "Girigius"
__version__ = "1"
__problem__ = "16"

Output:
Digit sum of 2^1000: 1366
Execution time: 0.00017118453979492188
"""

import time


def double(num):
    return num * 2


def square(num):
    return num ** 2


def power(base, exponent):
    curr_num = base
    curr_exp = 1

    while curr_exp < exponent:
        if curr_exp * 2 <= exponent:
            curr_num = square(curr_num)
            curr_exp = curr_exp * 2

        if curr_exp + 1 <= exponent:
            curr_num = double(curr_num)
            curr_exp = curr_exp + 1

    return curr_num


def solution():
    sum_digits = 0
    num = power(2, 1000)

    for i in str(num):
        sum_digits += int(i)

    return sum_digits


time.ctime(0)
start_time = time.time()
x = solution()
end_time = time.time()
print("Digit sum of 2^1000:", x)
print("Execution time:", end_time - start_time)
