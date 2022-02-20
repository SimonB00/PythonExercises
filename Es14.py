def no_duplicates_1(list):
    list.sort()
    result = []

    for i in range(len(list)):
        if i == len(list) - 1:
            result.append(list[i])
            break
        if list[i] != list[i+1]:
            result.append(list[i])
    return result

def no_duplicates_2(list):
    return set(list)
print(no_duplicates_1([1,1,2,3,4,5,6,6,10,8,9,10,4]))
print(no_duplicates_2([1,1,2,3,4,5,6,6,10,8,9,10,4]))