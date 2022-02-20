board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
print(board)
moves_left = 9

while moves_left != 0:
    x1 = int(input("Player 1, make your move. Choose the x coordinate: ")) + 1
    y1 = int(input("Now choose the y coordinate ")) + 1
    if board[x1][y1] == 0:
        board[x1][y1] = 'X'
    else:
        print('That square is already occupied.')
    moves_left -= 1
    print(board)

    x2 = int(input("Now it's your turn, player 2. Choose the x coordinate: ")) + 1
    y2 = int(input("Now choose the y coordinate ")) + 1
    if board[x1][y1] == 0:
        board[x2][y2] = 'O'
    else:
        print('That square is already occupied.')
    moves_left -= 1
    print(board)