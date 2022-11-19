# decorator that prints the name of the called function
from typing import Callable


def function_name(func: Callable):
    """
        A decorator that prints the name of the called function
    """
    def wrapper(*args):
        return f'Function name: {func.__name__}\nFunction result: {func(*args)} '
    return wrapper


@function_name
def my_sum(first_number: float, second_number: float) -> float:
    """
    A function that adds two numbers
    """
    return first_number + second_number


@function_name
def my_multiply(first_number: float, second_number: float) -> float:
    """
    A function that multiplies two numbers
    """
    return first_number * second_number


# testing the result
print(my_sum(10.5, 15))
print(my_multiply(3, 4))

