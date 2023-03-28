import math
def decomopose(number):
    digits = []
    while number >= 1:
        digit = number % 10
        digits.append(digit)
        number = math.floor(number / 10)
    return digits

x = decomopose(65454654)
x.reverse()
print(x)