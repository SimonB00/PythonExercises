def inverte_sentence(str):
    sentence = str.split()
    inverted = []

    for i in range(len(sentence)):
        inverted.append(sentence[-(i+1)])
    return inverted
str_ = input("Please write a long sentence: ")
print(' '.join(inverte_sentence(str_)))