from mammal import Mammal


class Water(Mammal):
    def __init__(self, origin: str, fins: int, sound: str, speed: float, vegetarian: bool,
                 pregnancy_period: int, breastfeeding: bool = True):
        super().__init__(origin, False, sound, speed, vegetarian, pregnancy_period, breastfeeding)
        self.__fins = fins

    @property
    def fins(self):
        """
        A method to get the number of fins
        """
        return self.__fins

    @fins.setter
    def fins(self, fins_number: int):
        """
        A method to change the number of fins
        """
        if fins_number > 1:
            self.__fins = fins_number
        else:
            print("You are not able to set this value to the number of fins")

    def swim(self):
        if self.__fins == 2:
            print("I swim on a long distance")
        else:
            print("I swim very fast")


if __name__ == '__main__':
    dolphin = Water("Ocean", 2, "Puuu", 100, False, 5, True)
    dolphin.fins = 0
    print(dolphin.fins)
    dolphin.swim()
