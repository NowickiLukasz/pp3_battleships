from random import randint

"""
Creates a list of lists in an 8 x 8 pattern to represent a playing board 
used in the game.
"""
player_board = []

for i in range(8):
    player_board.append([" "] * 8)




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
    for ship in range(10):
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

def check_if_hit_or_miss():
    pass


create_battleships(player_board)
print_game_board(player_board)
player_guess_input()