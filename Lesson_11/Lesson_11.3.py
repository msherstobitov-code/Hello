class Exception:
    def __init__(self, param=None):
        self.param = param

    def check_param(self):
        list = []
        while True:
            x = input('Введите значение: ')
            if x.isdigit() == True:
                list.append(x)
            if x == 'stop':
                print(list)
                break
            if x.isdigit() == False:
                print(f'Введённое значение не число')


a = Exception(1)
a.check_param()