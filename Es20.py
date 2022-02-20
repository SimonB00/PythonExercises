def num_search(list, num):
    list.sort()
    result = False
    for el in list:
        if el == num:
            result = True
            break
    return result
def num_search2(list, num):
    list.sort()
    result = False
    size = int(len(list))

    if num < list[int(size/2)]:
        list2 = [n for n in list if n < list[int(size/2)]]
        print(list2)
    if num > list[int(size/2)]:
        list3 = [n for n in list if n > list[int(size/2)]]
        print(list3)
    if list3[0]==num:
        result = True
    return result

print(num_search2([1,2,3,4,5,6,7],5))