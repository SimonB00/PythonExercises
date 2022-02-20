age = input("Hey. How old are you? ")
age = int(age)
year_100 = 2022 - age + 100
times = input("Hey many times do you want to read the message? ")
times = int(times)
for i in range(times):
    print("You'll be 100 in year:", end = ' ')
    print(year_100)