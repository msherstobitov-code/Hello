from abc import ABC, abstractmethod
class ACloth(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def calc_cloth(self):
        pass

class Coat(ACloth):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def calc_cloth(self):
        x = round((self.size / 6.5 + 0.5), 1)
        return x

class Suit(ACloth):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def calc_cloth(self):
        y = round((2 * self.height + 0.3), 2)
        return y

    def __add__(self, x, y):
        z = x + y
        return f'Потребуется {z}м2 ткани'

b = Coat('Пальто', 46)
print(b.calc_cloth())

a = Suit('Костюм', 1.7)
print(a.calc_cloth())

print(a.__add__(b.calc_cloth(),a.calc_cloth()))