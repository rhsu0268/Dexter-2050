# this is a program that allows users to play tic tac toe

# Important functions
# 1. Print the board
# 2. Allow players to take a turn
# 3. Check that the game is won
# 4. Initialize the board
# 5. Update the board

# create a global variable for gameboard
gameboard = [['-' for x in range(3)] for x in range(3)]
MAX_DEPTH = 5


# Fn: This function initalizes the gameboard
# Parameters: None
# Return: None
def init_board():

    # create a list of three lists
    board = []

    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append("-")

    print(board)


# Fn: This function welcomes the user
# Parameters: None
# Return None
def welcome():
    print("Welcome to Tic-Tac-Toe")


# Fn: This function prints the gameboard
# Parameters: gameboard
# Return: None
def print_board(gameboard):

    for i in range(3):
        print('|', end="")
        for j in range(3):
            print(gameboard[i][j] + '|', end="")
        print("")



# Fn: This function allows a player to make a move
# Parameters: gameboard, player (X or O)
# Return: None
def move(gameboard, player):

    move = check_user_input()

    # validate user input
    if (gameboard[move[0]][move[1]] == '-'):
        gameboard[move[0]][move[1]] = player
    else:
        # check to make sure the move is valid
        print("Sorry, your choice is already occupied. Choose another!")
        while True:
            result = check_user_input()
            if (gameboard[result[0]][result[1]] == '-'):
                gameboard[result[0]][result[1]] = player
                break
            print("Sorry, your choice is already occupied. Choose another!")

    #print(gameboard[row][col])

# Fn: This function checks that the user is making a valid move
# Parameters: None
# Return: Tuple containing row and col of the user's move
def check_user_input():
    while True:
        try:
            row = int(input("Input row: "))
            if (row < 0 or row > 2):
                print("Invalid value!")
                continue
            break
        except ValueError:
            print("Oops! That was not a valid index. Try again...")
            continue


    while True:
        try:
            col = int(input("Input col: "))
            if (col < 0 or col > 2):
                print("Invalid value!")
                continue
            break
        except ValueError:
            print("Oops! That was not a valid index. Try again...")
            continue
    return row, col


# Fn: This function switches the turn to X
# Parameters: None
# Return: None
def X_turn():
    print("It is X's turn.")

# Fn: This function switches the turn to O
# Parameters: None
# Return: None
def O_turn():
    print("It is O's turn.")

# Fn: This function checks that the game has been won
# Parameters: gameboard
# Return: Boolean (True or False)
def won(gameboard):
    i = 0

    for i in range(3):
        # check rows
        if (check_row(i)):
            return True

    for j in range(3):
        # check rows
        if (check_col(j)):
            return True
    if (check_diagonal()):
        return True
    return False

def check_row(row):
    # make sure that the blank spaces in the beginning does not result in a false win
    if (gameboard[row][0] == '-' and gameboard[row][1] == '-' and gameboard[row][2] == '-'):
        return False
    if (gameboard[row][0] == gameboard[row][1] and gameboard[row][1] == gameboard[row][2]):
        return True
    else:
        #print("Not won yet!")
        return False

def check_col(col):
    # make sure that the blank spaces in the beginning does not result in a false win
    if (gameboard[0][col] == '-' and gameboard[1][col] == '-' and gameboard[2][col] == '-'):
        return False
    if (gameboard[0][col] == gameboard[1][col] and gameboard[1][col] == gameboard[2][col]):
        return True
    else:
        #print("Not won yet!")
        return False

def check_diagonal():
    if (gameboard[0][0] == '-' and gameboard[1][1] == '-' and gameboard[2][2] == '-'):
        return False
    if (gameboard[0][0] == gameboard[1][1] and gameboard[1][1] == gameboard[2][2]):
        return True
    if (gameboard[0][2] == '-' and gameboard[1][1] == '-' and gameboard[2][0] == '-'):
        return False
    if (gameboard[0][2] == gameboard[1][1] and gameboard[1][1] == gameboard[2][0]):
        return True
    return False

def check_draw():
    for i in range(3):
        for j in range(3):
            if (gameboard[i][j] == '-'):
                return False
    return True


def minimax(gameboard, player, my_move, depth):

    if (depth > MAX_DEPTH):
        return 0

    # see if someone has won
    winner = won(gameboard)
    if (winner):
        


def play_game():
    welcome()
    while (True):
        #init_board()
        X_turn()
        print_board(gameboard)
        player = 'X'
        move(gameboard, player)
        if (won(gameboard)):
            print ("Congratulations! X wins the game!")
            return
        if (check_draw()):
            print("Great job to both! The game ends in a draw!")
            return
        print_board(gameboard)
        O_turn()
        player = 'O'
        move(gameboard, player)
        if (won(gameboard)):
            print ("Congratulations! O wins the game!")
            return
        if (check_draw()):
            print("Great job to both! The game ends in a draw!")
            return
        print(won(gameboard))
        print_board(gameboard)

play_game()