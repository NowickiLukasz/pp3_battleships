from random import randint

"""
Creates a list of lists in an 8 x 8 pattern to represent a playing board 
used in the game.
"""
player_board = []
for i in range(8):
    player_board.append([" "] * 8)

pc_board = []
for i in range(8):
    pc_board.append([" "] * 8)

player_guess_board = []
for i in range(8):
    player_guess_board.append([" "] * 8)


convert_to_numbers = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7
}


def print_game_board(game_board):
    """
    Prints a layout of the board game, with head legend.
    """
    print("  A B C D E F G H")
    print("  ===============")
    row = 1
    for i in game_board:
        print(row, "|".join(i))
        row += 1



def create_battleships(game_board):
    """
    Creates ships on the board randomly using row value and column value.
    10 ships created and labled with an "@", to show the location
    If "@" is already present, iterate again to find availabel space.
    """
    for ship in range(1):
        x_row = randint(0, 7)
        y_column = randint(0, 7)

        while game_board[x_row][y_column] == "@":
            x_row = randint(0, 7)
            y_column = randint(0, 7)
        
        game_board[x_row][y_column] = "@"
    


def player_guess_input():
    """
    Asks the user to enter a row number and a column letter
    if it is not valid, it will repeat the process untill the value is 
    correct
    """
    x_guess = input("Please enter a row number between 1-8 ")
    while x_guess not in "12345678":
        print("This is not a valid valid input. Enter value from 1-8 ")
        x_guess = input("Please enter a row number between 1-8 ")

    y_guess = input("Please enter a column letter between A-H ")
    while y_guess not in "ABCDEFGH":
        print("This is not a valid valid input. Enter value from A-H")
        y_guess = input("Please enter a column letter between A-H ")
    
    print(x_guess, y_guess)
    return int(x_guess) - 1, convert_to_numbers[y_guess]


def check_if_hit_or_miss():
    """
    Checks if user input matches location of hidden ship on the pc board.
    If input matches, marks location on the guess board, otherwise marks
    a miss. If the input has already been selected, asaks for inout again.
    """    
    x_guess, y_guess = player_guess_input()

    if (player_guess_board[x_guess][y_guess] == "X" or
        player_guess_board[x_guess][y_guess] == "-"):
        print("You have already used these co-ordinates. Please try again. ")
    elif pc_board[x_guess][y_guess] == "@":
        print("You have sank a ship")
        player_guess_board[x_guess][y_guess] = "X"
    else:
        print("You have missed")
        player_guess_board[x_guess][y_guess] = "-"

    print_game_board(player_guess_board)
    

create_battleships(pc_board)
create_battleships(player_board)
print("player Board")
print_game_board(player_board)
print_game_board(pc_board)
print("Guessing Board")
print_game_board(player_guess_board)
# player_guess_input()

check_if_hit_or_miss()