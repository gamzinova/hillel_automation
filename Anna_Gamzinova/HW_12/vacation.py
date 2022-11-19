import time
from abc import ABC

from icamping import ICamping
from ihiking import IHiking


# inheritance
class Vacation(ICamping, IHiking, ABC):
    def __init__(self, family_members: int, x: float, y: float):
        self.__vacation_period = 5
        if family_members > 0:
            self.__family_members = family_members
        else:
            raise ValueError("Number of family members should be higher than 0")
        self.__tent = False
        self.__fire = False
        if type(x) == float or type(x) == int:
            self.__x = x
        else:
            raise ValueError("Your coordinate x should be a number")
        if type(y) == float or type(y) == int:
            self.__y = y
        else:
            raise ValueError("Your coordinate y should be a number")

    @property
    def family_members(self):
        return self.__family_members

    @family_members.setter
    def family_members(self, new_number):
        if self.__family_members > 0:
            self.__family_members = new_number
        else:
            print("Number of family members can not be negative")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        if type(new_x) == float or type(new_x) == int:
            self.__x = new_x
        else:
            raise ValueError("Your coordinate x should be a number")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        if type(new_y) == float or type(new_y) == int:
            self.__y = new_y
        else:
            raise ValueError("Your coordinate y should be a number")

    # encapsulation
    def arrive_to_campsite(self):
        self.set_tent()
        self.set_campfire()
        self.barbeque()
        self.turn_off_campfire()

    # encapsulation
    def hiking(self):
        self.pack_tent()
        self.hike(self.__x, self.__y)
        self.singing()
        self.take_picture()

    # encapsulation
    def vacation(self):
        self.arrive_to_campsite()
        self.hiking()
        self.go_back_to_campsite()

    def set_tent(self):
        self.__tent = True
        print("Your tent is ready")

    def pack_tent(self):
        self.__tent = False
        print("The tent is packed")

    def set_campfire(self):
        self.__fire = True
        print("The heat is high, ready for the barbeque")

    def turn_off_campfire(self):
        self.__fire = False
        print("The fire is off")

    # polymorphism
    def singing(self):
        if self.__family_members > 1:
            print("La la la la")
        else:
            print("I do not sing alone")

    def barbeque(self):
        if self.set_campfire:
            print("The meat is on the grill")
            time.sleep(2)
            print("The meat is ready")

    def hike(self, x: float, y: float):
        self.__x += x
        self.__y += y
        print(f"We are hiiking! Our coordinates are {x} and {y})")

    # polymorphism
    def take_picture(self):
        if self.__family_members > 2:
            print("Say Cheeese!")
        elif self.__family_members == 1:
            print("Selfie tiiime!!!")

    def go_back_to_campsite(self):
        self.__x = 0
        self.__y = 0
        print("Back to the campsite!")


if __name__ == '__main__':
    my_vacation = Vacation(3, 32.997376, 35.687629)
    my_vacation.vacation()
