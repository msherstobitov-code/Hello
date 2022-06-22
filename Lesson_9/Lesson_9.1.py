import time
class TrafficLight:
    __color = ['red', 'yellow', 'green'] # создания атрибута класса (приватного)
    def __running(self): # создание метода класса
        print(mc._TrafficLight__color[0])
        time.sleep(7)
        print(mc._TrafficLight__color[1])
        time.sleep(2)
        print(mc._TrafficLight__color[2])
        time.sleep(4)
mc = TrafficLight() # создание экземпляра класса
mc._TrafficLight__running() #вызов экземпляра класса
