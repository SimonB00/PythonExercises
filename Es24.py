def grid(dimension):
    oriz = '---'
    vert = '|'

    for i in range(dimension):
        print(' ', end='')
        for j in range(dimension):
            print(oriz, end=' ')
        print('\n')
        print(vert, end='')
        for j in range(dimension):
            print('   ', end='')
            print(vert, end='')
        print('\n')
    print(' ', end='')
    for j in range(dimension):
        print(oriz, end=' ')
    print('\n')

dimension = input("How big should this n*n grid be? ")
dimension = int(dimension)   
grid(dimension)