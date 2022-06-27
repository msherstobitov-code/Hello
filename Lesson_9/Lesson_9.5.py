class Stationery:
    title = ['Pen', 'Pencil', 'Handle']

    def draw(self):
        print('Отрисовка класса Stationery')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка класса {Stationery.title[0]}')


class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка класса {Stationery.title[1]}')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка класса {Stationery.title[2]}')


a = Pen()
a.draw()
b = Pencil()
b.draw()
c = Handle()
c.draw()