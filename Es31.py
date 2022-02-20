def first_check(guess, word):
    result = ''
    for letter in word:
        if letter == guess:
            result = result + letter
        else:
            result = result + '_'
    return result
def subsequent_check(guess, word, previous):
    result = ''
    #list_of_guessed_letters = []
    #for letter in previous:
    #    if letter != '_':
    #        list_of_guessed_letters.append(letter)
    for i in range(len(word)):
        if previous[i] != '_':
            result = result + previous[i]
        if word[i] == guess:
            result = result + word[i]
        elif word[i] != guess and previous[i] == '_':
            result = result + '_'
    return result

attempt = 1
word_ = "SIMOSONATURA"
partial_solution = ''
while(True):
    guess_ = input("Guess a letter: ")
    if attempt == 1:
        print(first_check(guess_,word_))
        partial_solution = first_check(guess_,word_)
    else:
        print(subsequent_check(guess_, word_, partial_solution))
        partial_solution = subsequent_check(guess_, word_, partial_solution)
    attempt = attempt + 1
    
    if partial_solution == word_:
        print(word_)
        print("Congratulations, you've won!")
        exit()