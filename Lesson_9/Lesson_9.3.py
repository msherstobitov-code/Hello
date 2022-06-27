
class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 50000, 'bonus': 20000}

class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')
    def get_total_income(self):
        x = self._income['wage']
        y = self._income['bonus']
        print(f'{self.name} {self.surname} зарплата {x} руб., премия {y} руб.')

a = Position('Иванов', 'Иван', 'Инженер')
a.get_full_name()
b = Position('Птеров', 'Олег', 'Инженер')
b.get_total_income()