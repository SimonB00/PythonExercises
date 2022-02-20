def max(a,b,c):
    max = 0
    if a >= b:
        if a >= c: 
            max = a
        elif a < c:
            max = c
    else:
        if b >= c: 
            max = b
        elif b < c:
            max = c
    return max

print(max(3,5,4))