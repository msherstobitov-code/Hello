class Cell:

    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.get_size() + other.get_size())

    def __sub__(self, other):
        if self.get_size() < other.get_size():
            raise ValueError("cells can't be < 0")

        return Cell(self.get_size() - other.get_size())

    def __mul__(self, other):
        return Cell(self.get_size() * other.get_size())

    def __floordiv__(self, other):
        return Cell(self.get_size() // other.get_size())

    def get_cells(self):
        return str(self).replace("Cell(", "").replace(")", "")

    def get_size(self):
        return self.get_cells().count("*")

    def __str__(self):
        return f"Cell({'*' * self.cells})"

    def make_order(self, split_cell):

        if split_cell == 0:
            raise ValueError("can't split")

        if split_cell >= self.get_size():
            return self._get_cells()

        size = self.get_size()

        return "".join([f"{x}/n" if i % split_cell == 0 and i != size
                        else x
                        for i, x in enumerate(self.get_cells(), start=1)])


a = Cell(3)
b = Cell(2)
print(a + b)

c = Cell(12)
d = Cell(5)
print(c - d)

e = Cell(3)
f = Cell(5)
print(e * f)

g = Cell(12)
h = Cell(5)
print(g // h)

v = Cell(12)
print(v.make_order(5))