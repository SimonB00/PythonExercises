num = input("Think of a number. What is it? ")
num = int(num)

if ((num % 2) == 0) and ((num % 4) != 0):
    print("This number is even.")
elif ((num % 2) == 0) and ((num % 4) == 0):
    print("This number is a multiple of 4.")
else:
    print("This number is odd.")

check = input("You want to divide num by what? ")
check = int(check)

if (num % check) == 0:
    print("Congratulations. They divide evenly.")
else:
    print("Nope, sorry. They don't divide evenly.")