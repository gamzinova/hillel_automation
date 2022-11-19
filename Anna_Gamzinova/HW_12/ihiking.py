# abstraction
from abc import abstractmethod


class IHiking:
    @abstractmethod
    def set_destination(self):
        pass

    @abstractmethod
    def take_picture(self):
        pass

