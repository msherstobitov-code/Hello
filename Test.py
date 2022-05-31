numbers = {
           'zero': 'ноль',
           'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять'}

def num_translate(*args):
    while True:
        numeral = input('enter a number from the zero to ten: ')
        for key, value in numbers.items():
            if numeral == key:
                print(value)

num_translate()


