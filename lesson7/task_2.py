from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3


my_coat = Coat(169)
print(my_coat.consumption, end='\n\n')
my_costume = Costume(170)
print(my_costume.consumption)
