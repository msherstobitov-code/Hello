class Matrix:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        for line in self.param:
            for i in line:
                print(f"{i:4}", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.param)):
            for i_2 in range(len(other.param[i])):
                self.param[i][i_2] = self.param[i][i_2] +other.param[i][i_2]
            return Matrix.__str__(self)

a = Matrix([[3, 5, 1], [8, 6, 7], [2, 1, 9], [3, 5, 1]])
print(a)
new_a = Matrix([[7, 9, 2], [3, 0, 2], [2, 7, 8], [3, 2, 6]])
print(a.__add__(new_a))