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
    Returns values to be indexed from 0 value
    """
    x_guess = input("Please enter a row number between 1-8 \n")
    while x_guess not in "12345678":
        print("This is not a valid valid input. Enter value from 1-8 ")
        x_guess = input("Please enter a row number between 1-8 \n")

    y_guess = input("Please enter a column letter between A-H \n").upper()
    while y_guess not in "ABCDEFGH":
        print("This is not a valid valid input. Enter value from A-H")
        y_guess = input("Please enter a column letter between A-H \n").upper()
    
    return int(x_guess) - 1, convert_to_numbers[y_guess]


def check_if_hit_or_miss():
    """
    Checks if user input matches location of hidden ship on the pc board.
    If input matches, marks location on the guess board, otherwise marks
    a miss. If the input has already been selected, asks for inout again.
    Assign 20 rounds per game.
    """    
    round_number = 20
    ships_found = 0
    next_round = True

    while (round_number >= 0) & next_round:
        # sets values from the player input function
        x_guess, y_guess = player_guess_input()

        # checks if markers present, if yes, asks for repeat input
        if (player_guess_board[x_guess][y_guess] == "X" or
            player_guess_board[x_guess][y_guess] == "-"):
            print("You have already used these co-ordinates. Try again. \n")
            player_guess_input()

        # Checks if ship present, if yes, marks as hit, increments round
        # Increments score and runs pc guess function
        elif pc_board[x_guess][y_guess] == "@":
            print("You have sank a ship \n")
            player_guess_board[x_guess][y_guess] = "X"
            round_number -= 1
            ships_found += 1
            pc_guess_input()

        # Marks a missed guess
        else:
            print("You have missed")
            player_guess_board[x_guess][y_guess] = "-"
            round_number -= 1
            pc_guess_input()

        # checks if all ships have been found and shows instruction
        if ships_found == "10":
            print("You have found all of the ships. \n")
            break
        else:
            print(f"You have found {ships_found} ships. \n")
            print(f"There are {round_number} rounds remaining \n")

        # Checks if game is over by rounds remaining
        if round_number == 0:
            print("Game is now over, you have taken up all your moves \n")
            print("PC Ships Board \n")
            print_game_board(pc_board)
            break
        else:
            next_round = play_next_round()
            

def play_next_round():
    """
    Asks player if they want to keep on playing the game.
    This in turn stops the new boards been printed and helps the
    playher see what instructions the game gives
    """
    choice = input("Please enter YES for next round or NO to finish \n").upper()
    next_round = ["YES", "NO"]

    while choice not in next_round:
        choice = input("Please enter YES for next round or NO to finish \n").upper()
    if choice == "YES":
        print("player Board")
        print_game_board(player_board)
        print("Guessing Board")
        print_game_board(player_guess_board)
        return True
    else:
        print("You have ended the game on move \n")
        print("PC Ships Board")
        print_game_board(pc_board)
    return False


def pc_guess_input():
    """
    Allows the pc to randomly generate a guess to look for a ship
    on a player board.
    If a ship is found, it is marked with an X if missed with a -.
    """
    x_pc_rand = randint(0, 7)
    y_pc_rand = randint(0, 7)

    if (player_board[x_pc_rand][y_pc_rand] == "X" or
        player_board[x_pc_rand][y_pc_rand] == "-"):
        x_pc_rand = randint(0, 7)
        y_pc_rand = randint(0, 7)
    elif player_board[x_pc_rand][y_pc_rand] == "@":
        player_board[x_pc_rand][y_pc_rand] = "X"
    else:
        player_board[x_pc_rand][y_pc_rand] = "-"


def start_of_game():
    """
    Starts the game by printing welcome message and asking player for
    a username.
    Prints the boards the player will be playing on.
    """
    create_battleships(pc_board)
    create_battleships(player_board)
    print("player Board")
    print_game_board(player_board)
    print_game_board(pc_board)
    print("Guessing Board")
    print_game_board(player_guess_board)

start_of_game()
check_if_hit_or_miss()