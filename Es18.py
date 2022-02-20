import random

number = random.randint(1000,9999)
number = str(number)
print(number)
while(True):
    cow = 0
    bull = 0
    guess = input("Guess the number: ")
    if guess == number:
        cow = len(number)
        break
    for i in range(len(number)):
        if number[i]==guess[i]:
            cow = cow + 1
        else:
            for j in range(len(number)):
                if number[i]==guess[j]:
                    bull = bull + 1
                    break
    print("Cows = ", end='')
    print(cow)
    print("Bulls = ", end='')
    print(bull)

print("Cows = ", end='')
print(cow)  
print("Bulls = ", end='')
print(bull)