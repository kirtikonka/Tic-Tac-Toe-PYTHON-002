# displays board
# check wins(row, col, diagonals)
# flip player
# check tie
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
#Global Variable
game_on = True
winner = None
current_player = "X"
# this is what is diaplayed at the very beginning of the game
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    display_board()
    while game_on:
        handle_turn(current_player)
        game_over()
        flip_player()
    # this is what is displayed when the game is over
    if winner == "X" or winner == "O":
        print(winner + " won! Congratulations!")
    elif winner == None:
        print("Woah that's a Tie. Try again!")

# this handles the user input
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    # handles the turn of the player and takes care there is no input other than 1-9
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = print("Invalid Input. Choose a position from 1-9! Try again: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("That position is already taken. Try again!")
    board[position] = player
    display_board()

def game_over():
    check_win()
    check_tie()

def check_win():
    # global variable is called
    global winner
    row = check_row()
    col = check_col()
    diagonal = check_diagonals()
    if row:
        winner = row
    elif col:
        winner = col
    elif diagonal:
        winner = diagonal
    else:
        winner = None
    return

def check_row():
    # global variable is called
    global game_on
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #checks who won
    if row_1 or row_2 or row_3:
        game_on = False
    # returns the winner (X or O)
    if row_1:
        board[0]
    elif row_2:
        board[3]
    elif row_3:
        board[6]
    return

def check_col():
    # global variable is called
    global game_on
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    #checks who won
    if col_1 or col_2 or col_3:
        game_on = False
    # returns the winner (X or O)
    if col_1:
        board[0]
    elif col_2:
        board[1]
    elif col_3:
        board[2]
    return

def check_diagonals():
    # global variable is called
    global game_on
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    #checks who won
    if diagonal_1 or diagonal_2:
        game_on = False
    # returns the winner (X or O)
    if diagonal_1:
        board[0]
    elif diagonal_2:
        board[2]
    return

def check_tie():
    # global variable is called
    global game_on
    if "-" not in board:
        game_on = False
    return

def flip_player():
    # global variable is called
    global current_player
    # changes the player from X to O and vice versa
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()