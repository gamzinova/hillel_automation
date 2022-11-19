# abstraction
from abc import abstractmethod


class ICamping:
    @abstractmethod
    def set_tent(self):
        pass

    @abstractmethod
    def pack_tent(self):
        pass

    @abstractmethod
    def set_campfire(self):
        pass

    @abstractmethod
    def singing(self):
        pass

    @abstractmethod
    def barbeque(self):
        pass

