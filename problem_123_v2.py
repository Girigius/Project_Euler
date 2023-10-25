# Project Euler #123 #v2


import time

prime_cache = [2, 3]

def prime_gen():
    num = prime_cache[-1]
    curr_len = len(prime_cache)

    while len(prime_cache) < curr_len + 1:
        is_prime = True
        num += 2
        for i in range(3, num // 2 + 1, 2):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_cache.append(num)


def psr(n):
    while len(prime_cache) < n:
        prime_gen()

    return ((prime_cache[n - 1] - 1) ** n +
            (prime_cache[n - 1] + 1) ** n) % (prime_cache[n - 1] ** 2)


def solution(digit_len):
    n = 1
    while len(str(psr(n))) < digit_len:
        print(n)
        n += 1
    return n

time.ctime(0)
start_time = time.time()
print(solution(11))
end_time = time.time()
print(end_time - start_time)
print(prime_cache[-1])

# for i in range(100):
#     prime_gen()
#
# print(prime_cache)
