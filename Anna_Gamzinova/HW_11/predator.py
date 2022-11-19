from mammal import Mammal


class Predator(Mammal):
    def __init__(self, origin: str, legs: int, sound: str, speed: float, pregnancy_period: int,
                 animals_eaten_today: int, breastfeeding: bool = True):
        super().__init__(origin, legs, sound, speed, False, pregnancy_period, breastfeeding)
        self.__animals_eaten_today = animals_eaten_today

    @property
    def animals_eaten_today(self):
        """
        A method to get the predator's number of animals eaten
        """
        return self.__animals_eaten_today

    @animals_eaten_today.setter
    def animals_eaten_today(self, animals_eaten: int):
        """
        A method to change the predator's number of animals eaten
        """
        if animals_eaten > -1:
            self.__animals_eaten_today = animals_eaten
        else:
            print("You are not able to set a negative value to the predator's number of animals eaten")

    def is_hungry(self):
        if self.__animals_eaten_today < 1:
            print("I am very hungry")
        else:
            print("Im am full, I do not want to eat, thanks")

    def feed_me(self, animals: int = 1):
        """
        A method to feed the predator
        """
        if animals > -1:
            self.__animals_eaten_today += animals
        else:
            print("The number of animals can not be negative")


if __name__ == '__main__':
    tiger = Predator("Africa", 4, "Ararar", 150, 4, 10, True)
    tiger.is_hungry()
    tiger.feed_me(10)
    print(tiger.animals_eaten_today)
