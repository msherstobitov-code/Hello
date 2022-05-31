from random import choice # Import of necessary functions and modules

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n): # Declaring a joke generating function
    for i in range(n):
        random_index = choice(nouns) # Selecting a random word from the list nouns
        random_index_1 = choice(adverbs) # Selecting a random word from the list adverbs
        random_index_2 = choice(adjectives) # Selecting a random word from the list adjectives
        joke = "{} {} {}".format(random_index, random_index_1, random_index_2) # Making a string of selected words
        print(joke)

get_jokes(4) # Function call

