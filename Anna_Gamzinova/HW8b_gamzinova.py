# filter function
from typing import Callable


def filter_function(callback: Callable, sequence: iter) -> iter:
    """
    The filter function excludes items in an iterable object
    """
    # return eval(f"{callback}({sequence})")
    return [item for item in sequence if callback(item)]


# testing the function
def my_func(x):
    if x < 3:
        return False
    else:
        return True


my_list = [1, 2, 3, 4, 5]
print(filter_function(my_func, my_list))

