from functools import wraps

def type_logger(level=0):
    def logger(func):
        @wraps(func)
        def decor(*argv):
            if level > 0:
                return  ", ".join([f"{(x)}:{type(func(x))}" for x in argv])
        return decor
    return logger
@ type_logger(2)
def calc_cube(x):
    return x ** 3
a = calc_cube(5,4,6)
print(a)