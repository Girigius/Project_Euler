"""
__author__ = "George Ng"
__version__ = "1"

Problem number: 12

Output:
76576500  # Solution
[2, 2, 3, 3, 5, 5, 5, 7, 11, 13, 17]  # Prime factors of 76576500
576  # Number of factors in 76576500
0.2700960636138916  # Execution time
"""

import time

tri_cache = []
prime_cache = []


def gen_tri():
    if not tri_cache:
        tri_cache.append(1)
    else:
        tri_cache.append(tri_cache[-1] + len(tri_cache) + 1)


def prime_gen():
    curr_len = len(prime_cache)

    if not prime_cache:
        prime_cache.extend([2, 3])

    num = prime_cache[-1]

    while len(prime_cache) < curr_len + 1:
        is_prime = True
        num += 2
        for i in range(3, num // 2 + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_cache.append(num)


def prime_fact(n):
    curr_dividend = n
    new_dividend = n
    divisor_lst = []
    has_divisor = True
    if not prime_cache:
        prime_gen()
    while curr_dividend != 1:
        if not has_divisor:
            prime_gen()
        for i in prime_cache:
            if curr_dividend % i == 0:
                divisor_lst.append(i)
                new_dividend //= i
                has_divisor = True
                break
        if curr_dividend == new_dividend:
            has_divisor = False
        else:
            curr_dividend = new_dividend
    return divisor_lst


def prime_fact_to_num_fact(prime_fact_lst):
    prime_fact_dict = {}
    num_fact = 1

    for i in prime_fact_lst:
        if i in prime_fact_dict:
            prime_fact_dict[i] += 1
        else:
            prime_fact_dict[i] = 1

    for value in prime_fact_dict.values():
        num_fact *= value + 1

    return num_fact


def solution(n):
    num_divisor = 0
    last_tri = 0
    while num_divisor < n:
        num_divisor = 0
        gen_tri()
        last_tri = tri_cache[-1]
        num_divisor = prime_fact_to_num_fact(prime_fact(last_tri))
    return last_tri


time.ctime(0)
start_time = time.time()
x = solution(500)
end_time = time.time()
print(x)
print(prime_fact(x))
print(prime_fact_to_num_fact(prime_fact(x)))
print(end_time - start_time)
