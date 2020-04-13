import random
import time

class Person:
    def __init__(self, name, num, game_piece=None, color=None, wins=0):
        self.name = name
        self.num = num
        self.game_piece = game_piece
        self.color = color
        self.wins = wins

class Color:
    gray = '\033[90m'
    X = '\033[92m'
    O = '\033[94m'
    orange = '\033[33m'
    end = '\033[0m'

# Map for reference
pieces_map = (
    (7,8,9),
    (4,5,6),
    (1,2,3)
)

# Make a mutable list from the pieces_map tuple
def init_game(alist):
    return [list(row) for row in alist]

# Who goes first
def random_player():
    print("Randomly choosing who goes first...")
    time.sleep(wait)
    return random.randint(1, 2)

# Draw the tic-tac-toe board
def draw_board(p):

    # Always show the X player first in the stats
    if p1.game_piece == "X":
        px_name = p1.name
        px_wins = p1.wins
        po_name = p2.name
        po_wins = p2.wins
    else:
        px_name = p2.name
        px_wins = p2.wins
        po_name = p1.name
        po_wins = p1.wins

    # Colors for the board
    def c(i):
        if i == "X":
            return f"{Color.X}{i}{Color.end}"
        elif i == "O":
            return f"{Color.O}{i}{Color.end}"
        else:
            return f"{Color.gray}{i}{Color.end}"

    # Game board, grabbing values from pieces[]
    board = [
        [''],
        [f' {c(p[0][0])} ¡ {c(p[0][1])} ¡ {c(p[0][2])}      Total Wins'],
        [f'--=|=-=|=--    ------------'],
        [f' {c(p[1][0])} | {c(p[1][1])} | {c(p[1][2])}      {Color.X}{px_wins}{Color.end} : {Color.X}{px_name}{Color.end}'],
        [f'--=|=-=|=--     {Color.O}{po_wins}{Color.end} : {Color.O}{po_name}{Color.end}'],
        [f' {c(p[2][0])} ! {c(p[2][1])} ! {c(p[2][2])}      {Color.gray}{draw}{Color.end} : {Color.gray}Draws{Color.end}'],
        ['']
    ]

    for row in board:
        print(row[0])

# Get current player's name
def player_name(num):
    if p1.num == num:
        return f'{p1.color}{p1.name}{Color.end}'
    else:
        return f'{p2.color}{p2.name}{Color.end}'

# Get current player's game piece
def player_piece(num):
    if p1.num == num:
        return p1.game_piece
    else:
        return p2.game_piece

# Check the latest move
def check_move(spot, player):
    for rnum, row in enumerate(pieces_map):
        for inum, item in enumerate(row):
            # We are at the right row/col
            if spot == item:
                # If this spot is taken, they lose a turn
                if not isinstance(pieces[rnum][inum], int):
                    return "That one is taken! Saying goodbye to that turn..."
                else:
                    return (rnum, inum)

# Validate input
def get_input(type):

    fails = 0
    while True:
        if type == 'num':
            user_input = input('Choose a spot: ')
        else:
            user_input = input(f'Name of {type} player: ')

        try:
            if type == 'num':
                user_input = int(user_input)
                if user_input > 0 and user_input < 10:
                    return user_input
                else:
                    if fails == 0:
                        print(f"{Color.orange}Ahem... try entering a number between 1-9{Color.end}")
                        time.sleep(wait)
                    fails += 1
            else:
                if len(user_input) > 1:
                    return user_input
                else:
                    print(f"{Color.orange}A longer name would be nice...{Color.end}")
                    time.sleep(wait)
        except:
            if fails == 0:
                print(f'{Color.orange}Um... you need to enter a number{Color.end}')
                time.sleep(wait)
            fails += 1

        if fails == 2:
            print(f"{Color.orange}Looks like you're having a hard time figuring this out...{Color.end}")
            print(f"{Color.orange}Kissing that turn goodbye... NEXT!{Color.end}")
            time.sleep(wait)
            return False

# Check if someone has won
def check_win(p):
    # Check rows
    for rnum, row in enumerate(p):
        if row.count(row[0]) == 3:
            #print(f"WIN - row {rnum}")
            return "win"
    # Check cols
    for col in range(3):
        if [p[0][col], p[1][col], p[2][col]].count(p[0][col]) == 3:
            #print(f"WIN - col {col}")
            return "win"
    # Check diagonals
    if [p[0][0], p[1][1], p[2][2]].count(p[1][1]) == 3 or [p[0][2], p[1][1], p[2][0]].count(p[1][1]) == 3:
        #print(f"WIN - diag")
        return "win"
    # Check if full
    full = 0
    for row in p:
        for item in row:
            if item == "X" or item == "O":
                full += 1
    if full == 9:
        return "draw"

# Change player
def next_turn(num):
    if num == 1:
        return 2
    else:
        return 1

# Add win
def add_win(num):
    if num == 1:
        p1.wins += 1
    else:
        p2.wins += 1

# Whoever starts each game gets X
def init_players(num):
    if num == 1:
        p1.game_piece = "O"
        p1.color = Color.O
        p2.game_piece = "X"
        p2.color = Color.X
    else:
        p1.game_piece = "X"
        p1.color = Color.X
        p2.game_piece = "O"
        p2.color = Color.O

# Play again?
def play_again():
    choice = input("Play again? [Y/n] ").lower()
    if len(choice) == 0 or choice == 'y' or choice == 'yes':
        return True
    else:
        return False


# SETUP

print(f'\n{Color.X}===[ TIC-TAC-TOE ]==={Color.end}\n')

# Default pause after certain messages
wait = 2
time.sleep(wait)

# Total games that end in a draw
draw = 0

# Get player names
p1 = Person(get_input("first"), 1)
p2 = Person(get_input("second"), 2)

# Initialize game
turn = random_player()
pieces = init_game(pieces_map)
init_players(turn)
turn = next_turn(turn)

print(f"--> {player_name(turn)} won the toss and goes first!")
time.sleep(wait)


# Main game loop
while True:

    draw_board(pieces)

    print(f"--> {player_name(turn)}'s turn")

    # Get input for next move
    next_move = get_input('num')

    # >0 is success, otherwise they failed input validation
    if next_move > 0:
        # Check this move on the gameboard
        check = check_move(next_move, turn)
        # If there's an error, we'll get back a string
        if isinstance(check, str):
            print(f'{Color.orange}{check}{Color.end}')
            time.sleep(wait)
        # Otherwise, it will be a tuple with the list item to change
        elif isinstance(check, tuple):
            pieces[check[0]][check[1]] = player_piece(turn)


        # Check for win or draw
        if check_win(pieces) == "win":
            add_win(turn)
            draw_board(pieces)
            print(f'{player_name(turn)} wins!!')
            time.sleep(wait)
            if play_again():
                pieces = init_game(pieces_map)
                init_players(turn)
            else:
                break
        elif check_win(pieces) == "draw":
            draw += 1
            draw_board(pieces)
            print("It's a draw!!")
            if play_again():
                turn = random_player()
                pieces = init_game(pieces_map)
                init_players(turn)
            else:
                break

    # Next person's turn
    turn = next_turn(turn)

print("Ok, bye! *sniffle*")
