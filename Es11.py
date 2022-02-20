def divisors(num):
    list_of_div = []
    
    for i in range(num):
        if (num % (i+1)) == 0:
            list_of_div.append(i+1)
    return list_of_div

number = input("Please choose a number: ")
number = int(number)
is_prime = True

if (divisors(number)[0] == 1) and (divisors(number)[1] == number):
    is_prime = True
else:
    is_prime = False
print(is_prime)