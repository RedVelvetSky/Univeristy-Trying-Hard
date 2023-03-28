import random
import math
from math import sqrt, ceil

N = list(map(int, input().split()))

def is_prime(n):
    if n == 1:
        return False

    i = 2

    while i*i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

primes = set()

def sieveSundaram(MAX):
	
	marked = [False] * (int(MAX / 2) + 100)

	for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1):
		for j in range((i * (i + 1)) << 1,
						int(MAX / 2) + 1, 2 * i + 1):
			marked[j] = True

	primes.add(2)

	for i in range(1, int(MAX / 2) + 1):
		if (marked[i] == False):
			primes.add(2 * i + 1)

def sieve_of_atkin(end):
    """return a list of all the prime numbers <end using the Sieve of Atkin."""
    assert end > 0
    lng = (end - 1) // 2
    sieve = [False] * (lng + 1)

    x_max, x2, xd = int(sqrt((end - 1) / 4.0)), 0, 4
    for xd in range(4, 8 * x_max + 2, 8):
        x2 += xd
        y_max = int(sqrt(end - x2))
        n, n_diff = x2 + y_max * y_max, (y_max << 1) - 1
        if not (n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            m = n % 12
            if m == 1 or m == 5:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, x2, xd = int(sqrt((end - 1) / 3.0)), 0, 3
    for xd in range(3, 6 * x_max + 2, 6):
        x2 += xd
        y_max = int(sqrt(end - x2))
        n, n_diff = x2 + y_max * y_max, (y_max << 1) - 1
        if not (n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            if n % 12 == 7:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, y_min, x2, xd = int((2 + sqrt(4 - 8 * (1 - end))) / 4), -1, 0, 3
    for x in range(1, x_max + 1):
        x2 += xd
        xd += 6
        if x2 >= end:
            y_min = (((int(ceil(sqrt(x2 - end))) - 1) << 1) - 2) << 1
        n, n_diff = ((x * x + x) << 1) - 1, (((x - 1) << 1) - 2) << 1
        for d in range(n_diff, y_min, -8):
            if n % 12 == 11:
                m = n >> 1
                sieve[m] = not sieve[m]
            n += d

    primes = [2, 3]
    if end <= 3:
        return primes[: max(0, end - 2)]

    for n in range(5 >> 1, (int(sqrt(end)) + 1) >> 1):
        if sieve[n]:
            primes.append((n << 1) + 1)
            aux = (n << 1) + 1
            aux *= aux
            for k in range(aux, end, 2 * aux):
                sieve[k >> 1] = False

    s = int(sqrt(end)) + 1
    if s % 2 == 0:
        s += 1
    primes.extend([i for i in range(s, end, 2) if sieve[i >> 1]])

    return primes

def g(n):
    count = 0

    for number in range(1, n//2+1):
            difference = n - number
            # if is_prime(number, 4) and is_prime(difference, 4):
            #     count += 1
            if number in primes and difference in primes:
                count += 1
            # i += 1 
    return count 

primes = set(sieve_of_atkin(max(N)))

for i in N:
    print(g(i), end = (' '))