from enum import Enum


class TURN(Enum):
    LEFT = 0
    RIGHT = 1


class Car:
    speed = int
    colour = 'color'
    name = 'name'
    is_police: bool = False

    def __init__(self, colour, name):
        self.colour = colour
        self.name = name

    def go(self):
        print(f"{self.name} машина едет")

    def stop(self):
        print(f"{self.name} машина стоит")

    def turn(self, turn_side: TURN):
        print(f"{self.name} поворот на {turn_side.name}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, colour, name):
        super().__init__(colour, name)

    def show_speed(self):
        speed = super().show_speed()
        if speed > 40:
            print("Превышение сокости - 40 км/ч")
        return speed


class SportCar(Car):
    def __init__(self, colour, name):
        super().__init__(colour, name)


class WorkCar(Car):
    def __init__(self, colour, name):
        super().__init__(colour, name)

    def show_speed(self):
        speed = super().show_speed()
        if speed > 60:
            print("Превышение сокости - 60 км/ч")
        return speed


class PoliceCar(Car):
    def __init__(self, colour, name):
        super().__init__(colour, name)
        self.is_police = True


town_car = TownCar("white", "TownCar")
work_car = WorkCar("yellow", "WorkCar")
police_car = PoliceCar("Blue", "PoliceCar")

town_car.speed = 80
work_car.speed = 65
police_car.speed = 120

for some in [town_car, work_car, police_car]:
    print(f"машина - {some.name}")
    print(f"цвет городской машины - {some.colour}")
    print(f"это полицейская машина - {some.is_police}")
    some.go()
    some.stop()

    print(f"правый поворот - ", end="")
    some.turn(TURN.RIGHT)

    print(f"левый поворот - ", end="")
    some.turn(TURN.LEFT)

    print(f"скорость  - {some.show_speed()} км/ч", end="\n\n")