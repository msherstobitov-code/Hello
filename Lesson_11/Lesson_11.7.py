

class Complex_number:
    def __init__(self, param,):
        self.param = param

    def __add__(self, other):
        return self.param + other.param
    def __mul__(self, other):
        return self.param * other.param

a = Complex_number(2+1j)
b = Complex_number(3+2j)
print(a + b)
c = Complex_number(3+5j)
d = Complex_number(7+4j)
print(c * d)