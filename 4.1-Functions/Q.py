import math


def is_prime(number):
    if number == 1:
        return False
    n = int(math.sqrt(number))
    for i in range(2, n + 1):
        if number % i == 0:
            return False
    return True