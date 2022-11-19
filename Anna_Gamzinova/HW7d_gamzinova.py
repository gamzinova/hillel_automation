# Removing all the digits from the file with unknown length

import re


def no_digits(file_name: str) -> list:
    """
    The function removes all digits from the file
    """
    with open(file_name, "r") as my_file:
        lines = my_file.readlines()
        no_digit_file = []

        for line in lines:
            no_digit_file.append(re.sub(r"\d", r"", line))
    return no_digit_file

