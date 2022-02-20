import random
import time as tm
from os import system
cls = lambda: system('clear')

def pick_random_word(file):
    with open(file,'r') as open_file:
        list_of_words = open_file.read()
    list_of_words = list_of_words.split()
    number_of_words = len(list_of_words)
    index = random.randint(0,number_of_words - 1)

    return list_of_words[index]
def first_check(guess, word):
    result = ''
    for letter in word:
        if letter == guess:
            result += letter
        else:
            result += '_'
    return result
def subsequent_check(guess, word, previous):
    result = ''
    
    for i in range(len(word)):
        if previous[i] != '_':
            result += previous[i]
        if word[i] == guess:
            result += word[i]
        elif word[i] != guess and previous[i] == '_':
            result += '_'
    return result

attempt = 1
incorrect_attempts = 0
word_ = pick_random_word('List_of_words.txt').upper()
for i in range(len(word_)):
    print('_', end='')
print('\n')
partial_solution = ''
list_of_guesses = []
while(True):
    if incorrect_attempts == 1:
        print("  ____\n" + " |    |\n" + " |    \n" + " |   \n" + "_|_  /")
    if incorrect_attempts == 2:
        print("  ____\n" + " |    |\n" + " |    \n" + " |   \n" + "_|_  / \ ")
    if incorrect_attempts == 3:
        print("  ____\n" + " |    |\n" + " |    \n" + " |   -\n" + "_|_  / \ ")  
    if incorrect_attempts == 4:
        print("  ____\n" + " |    |\n" + " |    \n" + " |   - -\n" + "_|_  / \ ")
    if incorrect_attempts == 5:
        print("  ____\n" + " |    |\n" + " |    \n" + " |   -|-\n" + "_|_  / \ ")
    if incorrect_attempts == 6:
        print("You've lost!")
        print("  ____\n" + " |    |\n" + " |    o\n" + " |   -|-\n" + "_|_  / \ ")
        print(word_)
        break
    
    guess_ = input("Guess a letter: ")
    tm.sleep(0.1)
    cls()
    guess_ = guess_.upper()
    if guess_ != '' and len(guess_) == 1 and (guess_ in list_of_guesses) == False:
        if attempt == 1:
            print(first_check(guess_,word_))
            if partial_solution == first_check(guess_,word_):
                incorrect_attempts += 1
            partial_solution = first_check(guess_,word_)
        else:
            print(subsequent_check(guess_, word_, partial_solution))
            if partial_solution == subsequent_check(guess_,word_, partial_solution):
                incorrect_attempts += 1
            partial_solution = subsequent_check(guess_, word_, partial_solution)
        attempt = attempt + 1
        list_of_guesses.append(guess_)

        if partial_solution == word_:
            print(word_ + "\nContratulations, you've won!")
            break