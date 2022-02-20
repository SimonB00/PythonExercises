import random

def pick_random_word(file):
    with open(file,'r') as open_file:
        list_of_words = open_file.read()
    list_of_words = list_of_words.split()
    number_of_words = len(list_of_words)
    index = random.randint(0,number_of_words - 1)

    return list_of_words[index]

print(pick_random_word('List_of_words.txt'))