import random

def guess(range_min, range_max):
    return random.randint(range_min,range_max)

min = 1
max = 100
tries = 0
while(True):
    tries = tries + 1
    guess_ = guess(min,max)
    print(guess_)
    user_hint = input("Is this guess too high, too low or is it right? ")
    if user_hint == "right":
        print("Yay, I've won")
        print("It took me", end=' ')
        print(tries, end=' ')
        print("tries.")
        break
    if user_hint == "too high":
        max = guess_ - 1
    if user_hint == "too low":
        min = guess_ + 1