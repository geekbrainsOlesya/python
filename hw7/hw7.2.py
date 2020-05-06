from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, length):
        self.size = size
        self.length = length

    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def full(self):
        pass


class Coat(Clothes):
    @property
    def count(self):
        tissue = (self.size / 6.5 + 0.5)
        return f'На пальто {self.size} размера понадобится {tissue:.2f} м. ткани'

    def full(self):
        full_m = (self.size / 6.5 + 0.5) + (2 * self.length + 0.3)
        return full_m


class Suit(Clothes):
    @property
    def count(self):
        tissue = (2 * self.length + 0.3)
        return f'На костюм длиной {self.length} понадобится {tissue:.2f} м. ткани'

    def full(self):
        full_m = (self.size / 6.5 + 0.5) + (2 * self.length + 0.3)
        return f'Для пошива костюма и пальто понадобится ткани: {full_m:.2f} м.'


a = Coat(44,1.58)
print(a.count)
b = Suit(44,1.58)
print(b.count)
print(b.full())