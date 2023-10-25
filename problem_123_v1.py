# Project Euler #123


import time

cache = []


def factorial(n):
    p_odd = 1
    p_even = 1
    if n % 2 == 0:
        for i in range(3, n, 2):
            p_odd *= i
        for i in range(1, n // 2 + 1):
            p_even *= i
        return p_even * p_odd * (2 ** (n // 2))
    else:
        for i in range(3, n, 2):
            p_odd *= i
        for i in range(1, n // 2 + 1):
            p_even *= i
        return p_even * p_odd * (2 ** (n // 2)) * n


def is_prime(n):
    if (factorial(n - 1) + 1) % n == 0:
        return True
    else:
        return False


def psr(n):
    prime_list = [2]
    i = 3

    while len(prime_list) < n:
        if is_prime(i):
            prime_list.append(i)
        i += 2

    return ((prime_list[n - 1] - 1) ** n +
            (prime_list[n - 1] + 1) ** n) % (prime_list[n - 1] ** 2)


def solution(digit_len):
    n = 1
    while len(str(psr(n))) < digit_len:
        n += 1
        print(n)
    return n


# print(psr())
# digit_len = 11
time.ctime(0)
start_time = time.time()
solution(2)
end_time = time.time()
print(end_time - start_time)
