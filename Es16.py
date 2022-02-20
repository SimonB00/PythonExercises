import random

def pass_gen(length):
    symbols = ('~','`','!','@','#','$','%','^','&','*','(',')',
    '_','-','+','=','{','[','}',']','|','/',':',';','"',"'",'<',',','>','.','?')
    letters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u','v','w','x','y','z')
    password = []

    for char in range(length):
        select = random.randint(1,4)

        if select == 1:
            s = random.randint(0,30)
            password.append(symbols[s])
        elif select == 2:
            l = random.randint(0,25)
            password.append(letters[l])
        elif select == 3:
            l = random.randint(0,25)
            password.append(letters[l].upper())
        elif select == 4:
            n = random.randint(0,9)
            password.append(str(n))
    return password

while(True):
    need = input("Do you need a password? ")
    if need == "y" or need == "yes":    
        length = input("How long should the password be? ")
        length = int(length)
        print(''.join(pass_gen(length)))
    else:
        exit()