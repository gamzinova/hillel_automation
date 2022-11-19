from wagon import Wagon


class Train:
    def __init__(self, wagons: list):
        self.__wagons = wagons

    def __len__(self):
        return len(self.__wagons)

    @property
    def wagon_numbers(self):
        return [wagon.wagon_number for wagon in self.__wagons]

    def add_wagon(self, new_wagon: Wagon):
        """
        A method to add the number of wagons
        """
        if type(new_wagon) != Wagon:
            raise ValueError("You can add only a wagon")
        elif new_wagon.wagon_number in self.wagon_numbers:
            raise ValueError("The new wagon's number should be unique ")
        else:
            self.__wagons.append(new_wagon)

    def __str__(self):
        return ''.join(["<=[HEAD]", ''.join([f"-[{wagon_number}]" for wagon_number in sorted(self.wagon_numbers)])])


if __name__ == '__main__':
    # my_train = Train(10, 5)
    # print(len(my_train))
    my_wagons = [Wagon(10, 6), Wagon(2, 8)]
    my_train2 = Train(my_wagons)
    print(len(my_train2))
    # unable to add non Wagon
    # my_train2.add_wagon(2)
    # Unable to add non-unique wagon number
    # my_train2.add_wagon(Wagon(2, 5))
    my_train2.add_wagon(Wagon(3, 5))
    print(len(my_train2))
    print(my_train2)
