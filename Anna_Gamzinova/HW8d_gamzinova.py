# min and max functions


def max_function(sequence: iter, value: int = 1) -> iter:
    """
    The max function returns the largest item in an iterable
    """
    sorted_sequence = sorted(sequence, reverse=True)
    return sorted_sequence[:value]


def min_function(sequence: iter, value: int = 1) -> iter:
    """
    The min function returns the smallest item in an iterable
    """
    sorted_sequence = sorted(sequence, reverse=False)
    return sorted_sequence[:value]


# testing the result
numbers = [5, 10, 9, 1, 0, 8, 50]
names = ["Anna", "Yossi", "Tikva", "Barak"]
print(max_function(numbers, 2))
print(min_function(numbers, 3))
print(min_function(numbers))
print(max_function(names, 2))
print(min_function(names, 3))

