import random

def Rabin_Miller_Test(d, n):
    a = random.randrange(2, n-2)
    x = pow(a, d, n) # pow(base, exp, mod)
    if (x == 1 or x == n-1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
 
        if (x == 1):
            return False
        if (x == n - 1):
            return True

    return False

def is_prime (n, k):
    if (n <= 1 or n == 4): # quick dummy check
        return False
    if (n <= 3):
        return True

    d = n - 1
    while (d % 2 == 0):
        d //= 2
 
    for i in range(k):
        if (Rabin_Miller_Test(d, n) == False):
            return False
 
    return True

# def compute_goldbach_pair(number):
#     count = 0
#     for p1 in range(2, number):
#         p2 = number - p1
#         if is_prime(p1, 8) and is_prime(p2, 8):
#             count += 1
#     return count - 1

def goldbach(no):
  count = 0
  if no%2 !=0 :
    return 0
  elif no <= 2:
    return 0
  else:
      for i in range(3,no):
          if is_prime(i, 8) == 1:
              for l in range(i,no):
                  if is_prime(l, 8) == 1:
                      if no == (i+l):
                          count += 1
  return count

N = list(map(int, input().split()))

for i in N:
    print(goldbach(i), end = (' '))