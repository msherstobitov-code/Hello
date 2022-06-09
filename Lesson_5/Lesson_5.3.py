
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Максим',
    'Иван'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
def my_zip_gen():
    len_klasses = len(klasses)
    return ((tutors[i], klasses[i]) if i < len_klasses else (tutors[i], None)
            for i, j in enumerate(tutors))

if __name__ == '__main__':
    gen = my_zip_gen()
    print(type(gen))
    print(*gen)