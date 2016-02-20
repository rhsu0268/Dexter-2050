# this is a program that allows users to play tic tac toe

# Important functions
# 1. Print the board
# 2. Allow players to take a turn
# 3. Check that the game is won
# 4. Initialize the board
# 5. Update the board

# create a global variable for gameboard
gameboard = [['-' for x in range(3)] for x in range(3)]


def init_board():

    # create a list of three lists
    board = []

    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append("-")

    print(board)


# welcome the user
def welcome():
    print("Welcome to Tic-Tac-Toe")


def print_board(gameboard):

    for i in range(3):
        print('|', end="")
        for j in range(3):
            print(gameboard[i][j] + '|', end="")
        print("")

#print_board()


# allow the user to make a move
def move(gameboard, player):

    #gameboard = [[0 for x in range(3)] for x in range(3)]
    #print(gameboard)
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



    # validate user input
    #gameboard[2][2] = 'X'

    if (gameboard[row][col] == '-'):
        gameboard[row][col] = player
    else:
        # check to make sure the move is valid
        print("Sorry, your choice is already occupied. Choose another!")
        while True:
            result = check_user_input()
            if (gameboard[result[0]][result[1]] == '-'):
                gameboard[result[0]][result[1]] = player
                break
            print("Sorry, your choice is already occupied. Choose another!")

    print(gameboard[row][col])

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


def X_turn():
    print("It is X's turn.")

def O_turn():
    print("It is O's turn.")

# check that the game is not yet won
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