num = input("Give me a number: ")
num = int(num)

for i in range(num):
    if (num % (i+1)) == 0:
        print(i+1)