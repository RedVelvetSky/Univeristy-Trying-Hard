def is_prime(number):
    for div in range(2, number//2 + 1):
        if number % div == 0:
            return False
    return True


def compute_goldbach_pair(number):
    count = 0
    for p1 in range(2, number):
        p2 = number - p1
        if is_prime(p1) and is_prime(p2):
            count += 1
    return count - 1


print(compute_goldbach_pair(5))
print(compute_goldbach_pair(10))