from mammal import Mammal


class Flying(Mammal):
    def __init__(self, origin: str, legs: int, wings: int, sound: str, speed: float, vegetarian: bool,
                 pregnancy_period: int,
                 location_today: str, breastfeeding: bool = True):
        super().__init__(origin, legs, sound, speed, vegetarian, pregnancy_period, breastfeeding)
        self.__wings = wings
        self.__location_today = location_today

    @property
    def wings(self):
        """
        A method to get the number of wings
        """
        return self.__wings

    @wings.setter
    def wings(self, wings_number: int):
        """
        A method to change the number of wings
        """
        if wings_number > 1:
            self.__wings = wings_number
        else:
            print("You are not able to set this value to the number of wings")

    @property
    def location_today(self):
        """
        A method to get the animal's location today
        """
        return self.__location_today.capitalize()

    @location_today.setter
    def location_today(self, new_location: str):
        """
        A method to change the animal's location
        """
        if new_location:
            self.__location_today = new_location
        else:
            print("Your location is empty, can not update")

    def travel(self, destination):
        if self.__location_today == destination:
            print("I am already here, can't travel")
        elif not destination:
            print("Your destination is empty")
        else:
            print(f"Let's fly to {destination}")


if __name__ == '__main__':
    bat = Flying("Europe", 2, 2, "Click!", 80, False, 3, "Kyiv", True)
    bat.travel("Jerusalem")


