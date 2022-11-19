from animal import Animal


class Mammal(Animal):
    def __init__(self, origin: str, legs: int, sound: str, speed: float, vegetarian: bool, pregnancy_period: int,
                 breastfeeding: bool = True):
        super().__init__(origin, legs, sound, speed, vegetarian)
        self.__pregnancy_period = pregnancy_period
        self.__breastfeeding = breastfeeding

    @property
    def pregnancy_period(self):
        """
        A method to get the mammal's pregnancy period
        """
        return self.__pregnancy_period

    @pregnancy_period.setter
    def pregnancy_period(self, new_pregnancy_period: int):
        """
        A method to change the mammal's pregnancy period
        """
        if new_pregnancy_period > 0:
            self.__pregnancy_period = new_pregnancy_period
        else:
            print("You are not able to set a negative value to the mammal's pregnancy period")

    def new_life(self, current_pregnancy_period: int):
        if current_pregnancy_period > self.__pregnancy_period:
            print(f"{self.sound} hello world,I was born")
        else:
            print("I am still in mommy's tummy, see you soon!")

    @property
    def breastfeeding(self):
        """
        A method to get the mammals breastfeeding nature
        """
        return self.__breastfeeding

    @breastfeeding.setter
    def breastfeeding(self, is_breastfeeding: bool):
        """
        A method to update breastfeeding nature
        """
        self.__breastfeeding = is_breastfeeding

    def mammal(self):
        """
        A method to check id the animal is mammal
        """
        if self.__breastfeeding:
            print(f"{self.sound},nice to meet you, I am a mammal!")
        else:
            print("Sorry, I am not a mammal")


if __name__ == '__main__':
    elephant = Mammal("Africa", 4, "Pruu", 50, True, 2, True)
    elephant.predator()
    elephant.attack_sound()
    elephant.new_life(3)
