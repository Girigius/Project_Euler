"""
__author__ = "Girigius"
__version__ = "1"
__problem__ = "14"

Output:
Solution: 837799
Chain length of 837799: 525
Execution time: 10.727825164794922
"""


import time


def count_collatz_sequence(n):
    count = 1

    while n != 1:
        if n % 2 == 0:
            n //= 2
            count += 1
        else:
            n = 3 * n + 1
            count += 1

    return count


def solution():
    curr_longest = 0
    curr_longest_num = 0

    for i in range(1, 1000001):
        curr_count = count_collatz_sequence(i)

        if curr_count > curr_longest:
            curr_longest = curr_count
            curr_longest_num = i

    return curr_longest_num


time.ctime(0)
start_time = time.time()
x = solution()
end_time = time.time()
print("Solution:", x)
print("Chain length of 837799:", count_collatz_sequence(x))
print("Execution time:", end_time - start_time)


