dictionary = {'Simone': '04-12-2000', 'Alessandro': '22-05-2000', 'Lorenzo': '29-12-2000'}
name = input("This is the birthday dictionary. Whose birthday do you want to know? ")

if (name in dictionary) == False:
    print("I don't know this person.")
else:
    print(name, end='')
    print("'s birthday is ", end='')
    print(dictionary[name])