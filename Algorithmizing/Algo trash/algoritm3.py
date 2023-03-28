# import random
# import math
# # import array as arr
# import numpy as np
# # import itertools
# # import primes

# # def erat2( ):
# #     D = {  }
# #     yield 2
# #     for q in itertools.islice(itertools.count(3), 0, None, 2):
# #         p = D.pop(q, None)
# #         if p is None:
# #             D[q*q] = q
# #             yield q
# #         else:
# #             x = p + q
# #             while x in D or not (x&1):
# #                 x += p
# #             D[x] = p

# # def get_primes_erat(n):
# #   return list(itertools.takewhile(lambda p: p<n, erat2()))

# # import itertools
# # izip = itertools.zip_longest
# # chain = itertools.chain.from_iterable
# # compress = itertools.compress
# # def rwh_primes2_python3(n):
# #     """ Input n>=6, Returns a list of primes, 2 <= p < n """
# #     zero = bytearray([False])
# #     size = n//3 + (n % 6 == 2)
# #     sieve = bytearray([True]) * size
# #     sieve[0] = False
# #     for i in range(int(n**0.5)//3+1):
# #       if sieve[i]:
# #         k=3*i+1|1
# #         start = (k*k+4*k-2*k*(i&1))//3
# #         sieve[(k*k)//3::2*k]=zero*((size - (k*k)//3 - 1) // (2 * k) + 1)
# #         sieve[  start ::2*k]=zero*((size -   start  - 1) // (2 * k) + 1)
# #     ans = [2,3]
# #     poss = chain(izip(*[range(i, n, 6) for i in (1,5)]))
# #     ans.extend(compress(poss, sieve))
# #     return ans

# # N = list(map(int, input().split()))

# # def is_prime(n):
# #     if n < 2:
# #         return False
# #     for i in range(2, int(n ** 0.5) + 1):
# #         if n % i == 0:
# #             return False
# #     return True
    
# # def Rabin_Miller_Test(d, n):
# #     a = random.randrange(2, n-2)
# #     x = pow(a, d, n) # pow(base, exp, mod)
# #     if (x == 1 or x == n-1):
# #         return True
# #     while (d != n - 1):
# #         x = (x * x) % n
# #         d *= 2
 
# #         if (x == 1):
# #             return False
# #         if (x == n - 1):
# #             return True

# #     return False

# # def is_prime (n, k):
# #     if (n <= 1 or n == 4): # quick dummy check
# #         return False
# #     if (n <= 3):
# #         return True

# #     d = n - 1
# #     while (d % 2 == 0):
# #         d //= 2
 
# #     for i in range(k):
# #         if (Rabin_Miller_Test(d, n) == False):
# #             return False
 
# #     return True

# # def is_prime(n):
# #     """
# #     Assumes that n is a positive natural number
# #     """
# #     # We know 1 is not a prime number
# #     if n == 1:
# #         return False

# #     i = 2
# #     # This will loop from 2 to int(sqrt(x))
# #     while i*i <= n:
# #         # Check if i divides x without leaving a remainder
# #         if n % i == 0:
# #             # This means that n has a factor in between 2 and sqrt(n)
# #             # So it is not a prime number
# #             return False
# #         i += 1
# #     # If we did not find any factor in the above loop,
# #     # then n is a prime number
# #     return True


# # primes = np.array(2)
# primes = []

# # Utility function for Sieve of Sundaram
# def sieveSundaram(MAX):
	
# 	# In general Sieve of Sundaram, produces
# 	# primes smaller than (2*x + 2) for a
# 	# number given number x. Since we want
# 	# primes smaller than MAX, we reduce
# 	# MAX to half. This array is used to
# 	# separate numbers of the form i + j + 2*i*j
# 	# from others where 1 <= i <= j
# 	marked = [False] * (int(MAX / 2) + 100)

# 	# Main logic of Sundaram. Mark all
# 	# numbers which do not generate prime
# 	# number by doing 2*i+1
# 	for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1):
# 		for j in range((i * (i + 1)) << 1,
# 						int(MAX / 2) + 1, 2 * i + 1):
# 			marked[j] = True

# 	# Since 2 is a prime number
# 	primes.append(2)

# 	# Print other primes. Remaining primes
# 	# are of the form 2*i + 1 such that
# 	# marked[i] is false.
# 	for i in range(1, int(MAX / 2) + 1):
# 		if (marked[i] == False):
# 			primes.append(2 * i + 1)

# def g(n):

#     count = 0

#     for number in range(1, n // 2 + 1):
#             difference = n - number
#             if number in primes and difference in primes:
#                 count += 1

#     return count 

# # def get_primes(n):
# #   m = n+1
# #   #numbers = [True for i in range(m)]
# #   numbers = [True] * m #EDIT: faster
# #   for i in range(2, int(n**0.5 + 1)):
# #     if numbers[i]:
# #       for j in range(i*i, m, i):
# #         numbers[j] = False
# #   primes = []
# #   for i in range(2, m):
# #     if numbers[i]:
# #       primes.append(i)
# #   return primes

# # def primesfrom2to(n):
# #     # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
# #     """ Input n>=6, Returns an array of primes, 2 <= p < n """
# #     assert n >= 6
# #     sieve = np.ones(n // 3 + (n % 6 == 2), dtype=bool)
# #     sieve[0] = False
# #     for i in range(int(n ** 0.5) // 3 + 1):
# #         if sieve[i]:
# #             k = 3 * i + 1 | 1
# #             sieve[((k * k) // 3)::2 * k] = False
# #             sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False
# #     return np.r_[2, 3, ((3 * np.nonzero(sieve)[0] + 1) | 1)]

# N = list(map(int, input().split()))
# # primes = []
# # N = list(range(10000))
# # random.shuffle(N)

# # primes = tuple(primesfrom2to(max(N)+1))

# sieveSundaram(max(N))
# # tuple(primes)
# # # primes = tuple(rwh_primes2_python3(max(N)))
# # primes.sort

# # my_file = open("primes.txt", "w")
# # my_file.write(str(primes))
# # my_file.close()

# for i in N:
#     print(g(i), end = (' '))

import random
import math
from math import sqrt, ceil
# import numpy as np

N = list(map(int, input().split()))

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
    
# def Rabin_Miller_Test(d, n):
#     a = random.randrange(2, n-2)
#     x = pow(a, d, n) # pow(base, exp, mod)
#     if (x == 1 or x == n-1):
#         return True
#     while (d != n - 1):
#         x = (x * x) % n
#         d *= 2
 
#         if (x == 1):
#             return False
#         if (x == n - 1):
#             return True

#     return False

# def is_prime (n, k):
#     if (n <= 1 or n == 4): # quick dummy check
#         return False
#     if (n <= 3):
#         return True

#     d = n - 1
#     while (d % 2 == 0):
#         d //= 2
 
#     for i in range(k):
#         if (Rabin_Miller_Test(d, n) == False):
#             return False
 
#     return True

def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True

primes = set()

# # Utility function for Sieve of Sundaram
# def sieveSundaram(MAX):
	
# 	# In general Sieve of Sundaram, produces
# 	# primes smaller than (2*x + 2) for a
# 	# number given number x. Since we want
# 	# primes smaller than MAX, we reduce
# 	# MAX to half. This array is used to
# 	# separate numbers of the form i + j + 2*i*j
# 	# from others where 1 <= i <= j
# 	marked = [False] * (int(MAX / 2) + 100)

# 	# Main logic of Sundaram. Mark all
# 	# numbers which do not generate prime
# 	# number by doing 2*i+1
# 	for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1):
# 		for j in range((i * (i + 1)) << 1,
# 						int(MAX / 2) + 1, 2 * i + 1):
# 			marked[j] = True

# 	# Since 2 is a prime number
# 	primes.add(2)

# 	# Print other primes. Remaining primes
# 	# are of the form 2*i + 1 such that
# 	# marked[i] is false.
# 	for i in range(1, int(MAX / 2) + 1):
# 		if (marked[i] == False):
# 			primes.add(2 * i + 1)

def sieve_of_atkin(end):
    """return a list of all the prime numbers <end using the Sieve of Atkin."""
    # Code by Steve Krenzel, <Sgk284@gmail.com>, improved
    # Code: https://web.archive.org/web/20080324064651/http://krenzel.info/?p=83
    # Info: http://en.wikipedia.org/wiki/Sieve_of_Atkin
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
    for number in range(2, n // 2 + 1):
            difference = n - number
            if number in primes and difference in primes:
                count += 1
    return count 

primes = set(sieve_of_atkin(max(N)))

for i in N:
    print(g(i), end = (' '))
