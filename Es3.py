a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list = []
for el in a:
    if (el < 5) == True:
        print(el)
        list.append(el)
print(list)

list1 = [el for el in a if el < 5]
print(list1)

num = input("Give me a number: ")
num = int(num)

list2 = [el for el in a if el < num]
print(list2)