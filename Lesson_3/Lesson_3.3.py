def thesaurus(*args):
    dict = {}
    for name in args:
        key = name[0].capitalize()
        if key not in dict:
            dict[key] = []
        dict[key].append(name)
    return dict
print(thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Мойша', 'Павел', 'Анна', 'Акакий'))