def Fibonacci(nums):
    num1 = 0
    num2 = 1
    result = 0
    if nums == 1:
        return 1
    for i in range(nums - 1):
        result = num1 + num2
        num1 = num2
        num2 = result
    return result
    
print(Fibonacci(15))