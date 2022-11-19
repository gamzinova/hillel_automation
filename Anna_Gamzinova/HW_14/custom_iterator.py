import math


class CustomIterator:
    def __init__(self, sequence: list, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index > self.__end_index:
            raise ValueError("Please double check your indexes. Your start index is higher thn the end index.")
        elif math.fabs(self.__start_index) > len(self.__sequence):
            raise ValueError("Your start index is out of range")
        elif math.fabs(self.__end_index) > len(self.__sequence):
            raise ValueError("Your end index is out of range")
        elif self.__start_index < self.__end_index:
            number = self.__sequence[self.__start_index]
            self.__start_index += 1
            return number
        else:
            raise StopIteration


if __name__ == '__main__':
    custom_iterator = CustomIterator([1, 2, 3, 4, 5], -5, -2)

    for item in custom_iterator:
        print(item)
