with open('Text1.txt','r') as open_file1:
    list1 = open_file1.read()
with open('Text2.txt','r') as open_file2:
    list2 = open_file2.read()

list1 = list1.split(sep='\n')
list2 = list2.split(sep='\n')
overlapping_nums = []
for num1 in list1:
    for num2 in list2:
        if num1 == num2:
            overlapping_nums.append(num2)
print(overlapping_nums)