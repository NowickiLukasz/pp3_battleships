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
    print("A B C D E F G H")
    print("===============")
    row = 1
    for i in board:
        print(row, "|".join(i))



def create_battleships():
    pass


def player_guess_input():
    pass


def check_if_hit_or_miss():
    pass



print_game_board(player_board)