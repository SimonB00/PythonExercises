from os import system
cls = lambda: system('clear')

# Function printing the board
def grid(board):
    oriz = '---'
    vert = '|'

    for i in range(3):
        print(' ', end='')
        for j in range(3):
            print(oriz, end=' ')
        print('\n')
        print(vert, end='')
        for j in range(3):
            if board[i][j] == 0:
                print('   ', end='')
                print(vert, end='')
            else:
                print(' ' + str(board[i][j]) + ' ', end='')
                print(vert, end='')
        print('\n')
    print(' ', end='')
    for j in range(3):
        print(oriz, end=' ')
    print('\n')

# Function that calculates the total points in the rows
def row_sum(matrix):
    rows_sum = []
    for row in matrix:
        sum_ = sum(row)
        if (0 in row) == False:
            rows_sum.append(sum_)
        else:
            rows_sum.append(0)

    return rows_sum 

# Function that calculates the total points in the columns 
def column_sum(matrix):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for row in matrix:
        if row[0] != 0:
            sum1 += row[0]
        else:
            sum1 = 7
        if row[1] != 0:
            sum2 += row[1]
        else: 
            sum2 = 7
        if row[2] != 0:
            sum3 += row[2]
        else:
            sum3 = 7

    return [sum1, sum2, sum3]

# Function that calculates the total points in the diagonals
def diag_sum(matrix):
    diag1 = [matrix[0][0], matrix[1][1], matrix[2][2]]
    diag2 = [matrix[0][2], matrix[1][1], matrix[2][0]]
    if (0 in diag1) == False:
        sum1 = sum(diag1)
    else:
        sum1 = 0
    if (0 in diag2) == False:
        sum2 = sum(diag2)
    else:
        sum2 = 0

    return [sum1, sum2]
    
# Function that uses the previous function to find out who won
def player_won(matrix):
    rows_ = row_sum(matrix)
    cols_ = column_sum(matrix)
    diags_ = diag_sum(matrix)
    winner = 0

    if (3 in rows_) == True:
        winner = 1
    elif (6 in rows_) == True:
        winner = 2
    if (3 in cols_) == True:
        winner = 1
    elif (6 in cols_) == True:
        winner = 2
    if (3 in diags_) == True:
        winner = 1
    elif (6 in diags_) == True:
        winner = 2

    return winner

# Game building part
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
matrix = [[0,0,0],
          [0,0,0],
          [0,0,0]]
grid(board)
moves_left = 9

while moves_left != 0:
    c1 = 0
    c2 = 0
    while c1 == 0:
        x1 = int(input("Player 1, make your move. Choose the x coordinate: ")) - 1
        y1 = int(input("Now choose the y coordinate ")) - 1
        if x1 <= 3 and y1 <= 3:
            if board[x1][y1] == 0 and x1 < 3 and y1 < 3:
                board[x1][y1] = 'X'
                matrix[x1][y1] = 1
                c1 = 1
            elif board[x1][x2] != 0:
                print('That square is already occupied.')
        else:
            print('The x and y coordinate must have a value between 1 and 3.')
    moves_left -= 1
    cls()
    grid(board)
    if player_won(matrix) == 1:
        break
    while c2 == 0:
        x2 = int(input("Now it's your turn, player 2. Choose the x coordinate: ")) - 1
        y2 = int(input("Now choose the y coordinate ")) - 1
        if x2 <= 3 and y2 <= 3:
            if board[x2][y2] == 0 and x2 < 3 and y2 < 3:
                board[x2][y2] = 'O'
                matrix[x2][y2] = 2
                c2 = 1
            elif board[x1][x2] != 0:
                print('That square is already occupied.')
        else:
            print('The x and y coordinate must have a value between 1 and 3.')
    moves_left -= 1
    cls()
    grid(board)
    if player_won(matrix) == 2:
        break

print('The winner is player ' + str(player_won(matrix)))