
class Road:

    def __init__(self, length, width, thickness, specific_gravity):
        self._length = length
        self._width = width
        self._specific_gravity = specific_gravity
        self._thickness = thickness
        self.asphalt_mass = length * width * thickness * specific_gravity
    def __str__(self):
        return (f'Масса асфальта равна {self.asphalt_mass} т. ')

mass = Road(20, 5, 25, 5)
a = str(mass)
print(a)
