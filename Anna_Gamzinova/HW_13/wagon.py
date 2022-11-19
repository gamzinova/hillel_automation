class Wagon:
    def __init__(self, wagon_number: int, passengers: int):
        if (type(wagon_number) == int) and wagon_number > 0:
            self.__wagon_number = wagon_number
        else:
            raise ValueError("The wagon's number should be numeric")
        if (type(passengers) == int) and passengers > 0:
            self.__passengers = passengers
        else:
            raise ValueError("The passengers number should be numeric")

    @property
    def wagon_number(self):
        return self.__wagon_number

    @wagon_number.setter
    def wagon_number(self, new_wagon_number):
        if (type(new_wagon_number) == int) and new_wagon_number > 0:
            self.__wagon_number = new_wagon_number
        else:
            print("The new wagon's number should be numeric and higher than 0")

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, new_passengers_number):
        if (type(new_passengers_number) == int) and new_passengers_number > 0:
            self.__passengers = new_passengers_number
        else:
            print("The new passenger's number should be numeric and higher than 0")

    def add_passenger(self, passenger_number: int = 1):
        """
        A method to add the number of passengers
        """
        if type(passenger_number) == int and passenger_number > 0 and (self.__passengers + passenger_number) < 11:
            self.__passengers += passenger_number
        else:
            print(
                f"The new passenger's number should be numeric and total number should not exceed 10.\n"
                f"Current number of passengers is {self.__passengers} ")

    def __len__(self):
        return self.__passengers


if __name__ == '__main__':
    wagon = Wagon(3, 5)
    print(len(wagon))
    wagon.add_passenger(6)
    wagon.add_passenger(3)
    print(wagon.passengers)
