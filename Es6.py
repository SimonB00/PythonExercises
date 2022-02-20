str = input("Write a string: ")
result = True
if (len(str) % 2) == 0:
    for i in range(int(len(str)/2)):
        if str[i] == str[-(i+1)]:
            result = True
        else:
            result = False
else:
    for i in range(int(len(str)/2 - 0.5)):
        if str[i] == str[-(i+1)]:
            result = True
        else:
            result = False
print(result)
