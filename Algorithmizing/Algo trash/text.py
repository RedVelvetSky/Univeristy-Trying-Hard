import random
import math

N = list(map(int, input().split()))

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

# Utility function for Sieve of Sundaram
def sieveSundaram(MAX):
	
	# In general Sieve of Sundaram, produces
	# primes smaller than (2*x + 2) for a
	# number given number x. Since we want
	# primes smaller than MAX, we reduce
	# MAX to half. This array is used to
	# separate numbers of the form i + j + 2*i*j
	# from others where 1 <= i <= j
	marked = [False] * (int(MAX / 2) + 100)

	# Main logic of Sundaram. Mark all
	# numbers which do not generate prime
	# number by doing 2*i+1
	for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1):
		for j in range((i * (i + 1)) << 1,
						int(MAX / 2) + 1, 2 * i + 1):
			marked[j] = True

	# Since 2 is a prime number
	primes.add(2)

	# Print other primes. Remaining primes
	# are of the form 2*i + 1 such that
	# marked[i] is false.
	for i in range(1, int(MAX / 2) + 1):
		if (marked[i] == False):
			primes.add(2 * i + 1)


def g(n):
    count = 0
    # for i in range(2, N // 2 + 1):
    #     if is_prime(i, 4) and is_prime(N - i, 4):
    #         count += 1
    # return count

    for number in range(1, n//2+1):
            difference = n - number
            # if is_prime(number, 4) and is_prime(difference, 4):
            #     count += 1
            if number in primes and difference in primes:
                count += 1
            # i += 1 
    return count 

sieveSundaram(max(N))

for i in N:
    print(g(i), end = (' '))

