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

    row = int(input("Input row: "))
    if (row < 0 or row > 3):
        print("Invalid value!")
        return
    col = int(input("Input column: "))
    if (col < 0 or col > 3):
        print("Invalid value!")
        return


    # validate user input
    #gameboard[2][2] = 'X'

    # check to make sure the move is valid
    if (gameboard[row][col] == '-'):
        gameboard[row][col] = player
    else:
        print("That is an invalid move!")

    print(gameboard[row][col])


def X_turn():
    print("It is X's turn.")

def Y_turn():
    print("It is Y's turn.")

# check that the game is not yet won
def won(gameboard, row):

    for i in row:
        # check rows
        check_row(row)

def check_row(row):
        if (gameboard[row][0] == gameboard[row][1] and gameboard[row][1] == gameboard[row][2]):
            return 1
        else:
            return 0

def play_game():
    welcome()
    while (True):
        #init_board()
        X_turn()
        print_board(gameboard)
        player = 'X'
        move(gameboard, player)
        print_board(gameboard)
        Y_turn()
        player = 'O'
        move(gameboard, player)
        print_board(gameboard)

play_game()