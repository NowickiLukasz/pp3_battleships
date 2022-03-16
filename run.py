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

next_round = ["YES", "NO"]
start_or_rules = ["YES", "RULES"]
# PC_GUESS_SCORE = 0


def print_game_board(game_board):
    """
    Prints a layout of the board game, with head legend.
    """
    print("  A B C D E F G H")
    print("  ===============")
    row_number = 1
    for row in game_board:
        print(row_number, "|".join(row))
        row_number += 1


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
    y_guess = input("Please enter a column letter between A-H \n").upper()
    while y_guess not in "ABCDEFGH" or len(y_guess) > 1 or y_guess == "":
        print("This is not a valid valid input. Enter value from A-H")
        y_guess = input("Please enter a column letter between A-H \n").upper()

    x_guess = input("Please enter a row number between 1-8 \n")
    while x_guess not in "12345678" or len(x_guess) > 1 or x_guess == "":
        print("This is not a valid valid input. Enter value from 1-8 ")
        x_guess = input("Please enter a row number between 1-8 \n")
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
    # global PC_GUESS_SCORE
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
        if ships_found == 10:
            print("You have found all of the ships. \n")
            print("PC Board")
            print_game_board(pc_board)
            print("player Board")
            print_game_board(player_guess_board)
            break
        else:
            print(f"You have found {ships_found} ships. \n")
            print(f"There are {round_number} rounds remaining \n")

        # Checks if game is over by rounds remaining
        if round_number == 0:
            print("Game is now over, you have taken up all your moves \n")
            print("PC Ships Board \n")
            print_game_board(pc_board)
            print("Player Guess Board \n")
            print_game_board(player_guess_board)
            break
        else:
            next_round = play_next_round()


def play_next_round():
    """
    Asks player if they want to keep on playing the game.
    This in turn stops the new boards been printed and helps the
    playher see what instructions the game gives
    """
    choice = input(
        "Please enter YES for next round or NO to finish \n").upper()
    next_round = ["YES", "NO"]
    
    while choice not in next_round:
        validate_round_input(choice)
        choice = input(
            "Please enter YES for next round or NO to finish \n").upper()

    if choice == "YES":
        print("player Board")
        print_game_board(player_board)
        print("Guessing Board")
        print_game_board(player_guess_board)
        return True

    else:
        print("You have ended the game. \n")
        print("PC Ships Board")
        print_game_board(pc_board)
    return False


def validate_round_input(value):
    """
    validates input if player wants to continue round
    """
    try:
        if value not in next_round or value == "":
            print(f"Input provided is incorrect. You gave {value}.")
    except KeyError:
        print("Sorry please try again")


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
        # global PC_GUESS_SCORE += 1
    else:
        player_board[x_pc_rand][y_pc_rand] = "-"


def main_menu():
    """
    Prints query to user if the want to play or see the rules.
    """
    # start_or_rules = ["YES", "RULES"]

    print("Welcome to the battle ships game")
    print("If you want to start say YES")
    print("For rules say RULES")

    menu_start = input(
        "Say YES to start the game or RULES to learn the game \n").upper()

    while menu_start not in start_or_rules:
        validate_start_menu(menu_start)
        menu_start = input(
        "Say YES to start the game or RULES to learn the game \n").upper()
        
    if menu_start == "YES":
        start_of_game()
        check_if_hit_or_miss()
    elif menu_start == "RULES":
        game_rules()
    

def validate_start_menu(value):
    """
    If values entered not in start_or_rules print error
    """
    # start_or_rules = ["YES", "RULES"]
    try:
        if value not in start_or_rules or value == "":
            print(f"Input provided is incorrect. You gave {value}.")
    except KeyError:
        print("Sorry please try again")

def game_rules():
    """
    Prints rules for the game
    """
    start = ["START"]

    print("Welcome to the game of battle ships. \n ")
    print("Here are the game rules \n")
    print("You and your opponent have a board and some ships,")
    print("Use row numbers or column letters to find the ships. \n")
    print("And remember, to say YOU SANK MY BATTLESHIP! once a ship is sunk")

    game_start = input("Type START to begin the game. \n").upper()
    while game_start not in start:
        print(f"Please enter START to begin the game. You typed {game_start}")
        game_start = input("Type START to begin the game.").upper()
    if game_start == "START":
        start_of_game()
        check_if_hit_or_miss()


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


main_menu()
# play_next_round()
# play_next_round()