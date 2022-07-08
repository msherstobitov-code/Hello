class Error:
    def __init__(self, param_1 = None, param_2 = None):
        self.param_1 = param_1
        self.param_2 = param_2
    def div(self, param_1, param_2):
        try:
            result = param_1 / param_2
        except ZeroDivisionError:
            return "division by zero!"
        else:
            return f'result is, {result}'

a = Error()
print(a.div(25,5))
print(a.div(25,0))
