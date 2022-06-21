from functools import wraps
def val_checker(func_filter):
    def checker(func):
        @wraps(func)
        def decorator(x):
            if func_filter(x):
                return func(x)
            msg = f'ValueError: wrong val{x}'
            raise ValueError(msg)
        return decorator
    return checker
@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3
a = calc_cube(5)
#a = calc_cube(-9)
print(a)