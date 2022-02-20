import json

with open("birthdays.json", "r") as f:
    birthdays = json.load(f)

while(1):
    name = input("This is the birthday dictionary. Whose birthday do you want to know? (Write exit if you want to close the program) ")

    if(name == "Exit"):
        break
    if (name in birthdays) == False:
        print("I don't know this person.")
        birthday_ = input("What's their birthday? ")
        birthdays[name] = birthday_
        print("They have been added to the list.")
        with open('birthdays.json','w') as f:
            json.dump(birthdays, f)
    else:
        print(name, end='')
        print("'s birthday is ", end='')
        print(birthdays[name])