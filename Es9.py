import random

a = random.randint(1,9)
tries = 0

while 1 > 0:
    guess = input("Guess a number, or write 'exit' if you want to stop: ")
    if guess == "exit":
        break
    else: 
        guess = int(guess)

    if a == guess:
        print("Wow, great job!")
        tries = tries + 1
        break
    elif guess < a:
        print("Try guessing a little higher.")
        tries = tries + 1
    elif guess > a:
        print("Try guessing a little lower.")
        tries = tries + 1
print("It took you", end=' ')
print(tries, end=' ')
print("tries.")
