# all function

def all_function(sequence: iter) -> bool:
    """
    This function returns True if all items in an iterable object are true, otherwise returns False
    """
    for element in sequence:
        if not element:
            return False
    return True


# testing the result
mylist = [0, 1, 1]
mylist_true = [1, 1, 1]
print(all_function(mylist))
print(all_function(mylist_true))

