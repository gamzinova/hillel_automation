import math


def square(side_length: float) -> tuple:
    """"
    The function returns perimeter, area and diagonal of the square
    """
    return 4 * side_length, side_length ** 2, side_length * math.sqrt(2)


# Printing the result in tuple
print(square(3))

