from random import randint

"""
Creates a list of lists in an 8 x 8 pattern to represent a playing board 
used in the game.
"""
player_board = []

for i in range(8):
    player_board.append([" "] * 8)




def print_game_board(board):
    """
    Prints a layout of the board game, with head legend.
    """
    print("  A B C D E F G H")
    print("  ===============")
    row = 1
    for i in board:
        print(row, "|".join(i))
        row += 1



def create_battleships(board):
    """
    Creates ships on the board randomly using row value and column value.
    10 ships created and labled with an "@", to show the location
    """
    for ship in range(10):
        x_row = randint(0, 7)
        y_column = randint(0, 7)

        while board[x_row][y_column] == "@":
            x_row = randint(0, 7)
            y_column = randint(0, 7)
        
        board[x_row][y_column] = "@"
    


def player_guess_input():
    pass


def check_if_hit_or_miss():
    pass


create_battleships(player_board)
print_game_board(player_board)