# map function
from typing import Callable


def map_function(callback: Callable, sequence: iter) -> iter:
    """
    The map function executes a specified function for each item in an iterable.
    """
    return [callback(item) for item in sequence]


def square_func(number):
    return number * number


def lower_func(value):
    return value.lower()


numbers = range(1, 11)
float_numbers = [1.5, 2.9, 0.001]
my_sequence = ['Bike', 'Boat', 'Tent']

print(map_function(square_func, numbers))
print(map_function(square_func, float_numbers))
print(map_function(lower_func, my_sequence))
