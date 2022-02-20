player1 = input("First player, what do you choose? ")
if (player1 != "paper") or (player1 != "rock") or (player1 != "scissors"):
    print("First player, insert a valid option for this game, please.")
    exit()
player2 = input("Second player, what do you choose? ")
if player2 != "paper" or player2 != "rock" or player2 != "scissors":
    print("Second player, insert a valid option for this game, please.")
    exit()

if player1 == player2:
    print("It's a tie.")
if player1 == "rock":
    if player2 == "paper":
        print("Player2 wins.")
    if player2 == "scissors":
        print("Player1 wins.")
if player1 == "paper":
    if player2 == "rock":
        print("Player1 wins.")
    if player2 == "scissors":
        print("Player2 wins.")
if player1 == "scissors":
    if player2 == "rock":
        print("Player2 wins.")
    if player2 == "paper":
        print("Player1 wins.")