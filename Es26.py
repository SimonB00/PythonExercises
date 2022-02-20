def row_sum(matrix):
    rows_sum = []
    for row in matrix:
        sum_ = sum(row)
        if (0 in row) == False:
            rows_sum.append(sum_)
        else:
            rows_sum.append(0)

    return rows_sum  
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
    
    if winner == 1:
        print("Player 1 is the winner.")
    elif winner == 2:
        print("Player 2 is the winner.")
    elif winner == 0:
        print("It's a tie.")

game = [[1, 2, 0],
	    [2, 1, 0],
	    [2, 1, 1]]
winner_is_2 = [[2, 2, 0],
	           [2, 1, 0],
	           [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	           [2, 1, 0],
	           [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	                [2, 1, 0],
	                [2, 1, 1]]

no_winner = [[1, 1, 0],
	         [0, 2, 0],
	         [0, 0, 0]]

also_no_winner = [[1, 2, 0],
	              [2, 1, 0],
	              [2, 1, 0]]

player_won(winner_is_2)
player_won(game)
player_won(winner_is_1)
player_won(winner_is_also_1)
player_won(no_winner)
player_won(also_no_winner)
