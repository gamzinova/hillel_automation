class Animal:
    def __init__(self, origin: str, legs: int, sound: str, speed: float, vegetarian: bool):
        self.__origin = origin
        self.__legs = legs
        self.__sound = sound
        self.__speed = speed
        self.__vegetarian = vegetarian

    @property
    def origin(self):
        """
        A method to get animal's origin
        """
        return self.__origin.capitalize()

    @origin.setter
    def origin(self, new_origin: str):
        """
        A method to change the animal's origin
        """
        if new_origin:
            self.__origin = new_origin
        else:
            print("Your origin is empty, can not update")

    @property
    def legs(self):
        """
        A method to get the number of legs
        """
        return self.__legs

    @legs.setter
    def legs(self, legs_number: int):
        """
        A method to change the number of legs
        """
        if legs_number > -1:
            self.__legs = legs_number
        else:
            print("You are not able to set a negative value to the number of legs")

    @property
    def sound(self):
        """
        A method to get the animal's sound
        """
        return self.__sound.capitalize()

    @sound.setter
    def sound(self, new_sound: str):
        """
        A method to change the animal's sound
        """
        if new_sound:
            self.__sound = new_sound
        else:
            print("Your sound is empty, can not update")

    def attack_sound(self):
        """
        A method to change the animal's sound in case of attack
        """
        if not self.__vegetarian:
            print(f"{self.__sound} watch out, I am going to attack you!")
        else:
            print(f"{self.__sound} I will not attack you, let's be friends!")

    @property
    def speed(self):
        """
        A method to get the animal's speed
        """
        return self.__speed

    @speed.setter
    def speed(self, new_speed: float):
        """
        A method to change the animal's speed
        """
        if new_speed > -1:
            self.__speed = new_speed
        else:
            print("You are not able to set a negative value to the animal's speed")

    def speed_up(self, new_speed: float = 10):
        """
        A method to increase animal's speed. By default, the speed is increasing by adding a value 10.
        """
        if new_speed > -1:
            self.__speed += new_speed
        else:
            print("The speed can not be negative")

    @property
    def vegetarian(self):
        """
        A method to get the animal's diet
        """
        return self.__vegetarian

    @vegetarian.setter
    def vegetarian(self, is_vegetarian: bool):
        """
        A method to update the animal's diet
        """
        self.__vegetarian = is_vegetarian

    def predator(self):
        """
        A method to check if the animal is predator
        """
        if not self.__vegetarian:
            print(f"{self.__sound},I love meat!")
        else:
            print("Yuk, I do not eat meat!")


if __name__ == '__main__':
    lion = Animal("africa", 4, "Roar!", 100, False)
    print(lion.origin)
    lion.origin = "australia"
    print(lion.origin)
    lion.origin = ""
    lion.attack_sound()
    lion.speed_up(50)
    print(lion.speed)
    # lion.vegetarian = True
    # print(lion.vegetarian)
    lion.predator()
