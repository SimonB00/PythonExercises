a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
result = []

for el1 in a:
    for el2 in b:
        if el1 == el2:
            c.append(el2)
            break
for i in range(len(c)):
    if i == len(c)-1:
        result.append(c[i])
        break
    if c[i] != c[i+1]:
        result.append(c[i])
print(c)
print(result)