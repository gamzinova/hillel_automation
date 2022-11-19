# is_prime function
from typing import Union


def is_prime(number: int) -> Union[bool, str]:
    """
    The function checks if the number is prime
    """
    prime = True
    if number in range(2, 1001):
        for n in range(2, int(number/2)):
            if number % n == 0:
                prime = False
                break
        return prime
    else:
        return "Number is not in range"


# testing the result
print(is_prime(1))
print(is_prime(1000))
print(is_prime(5))
print(is_prime(10))
print(is_prime(19))
print(is_prime(2))

