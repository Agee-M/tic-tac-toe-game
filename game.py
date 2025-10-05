# TODO: Tic-tac-toe game implementation

def game():
    start()


def start():
    print("New Game")
    
    # Initialize new board
    board = new_board()
    print_board(board) # DEBUG

    #Initialize players
    # player()

def player():
    # Assign player names and characters
    players = {}
    players["Player1"] = [input("Player 1: "), 0]
    
    # Validate character
    valid = ["X", "O"]
    while True:
        try:
            # Assign player 1 choice
            choice = input("Pick X or O: ").upper()
        except ValueError:
            print("Needs to be a letter")
        if choice not in valid:
            print("Invalid choice")
        else:
            players["Player1"][1] = choice
            print(f"{players["Player1"][0]} is {choice}")
            break
    
    # Assign player 2 choice
    players["Player2"] = [input("Player 2: "), 0]
    if choice == "X":
        players["Player2"][1] = "O"
    else:
        players["Player2"][1] = "X"
    print(f"{players["Player2"][0]} is {players["Player2"][1]}")
    players["Player2"][1] = "O"


def score():
    pass

def new_board():
    # Creates 3 x 3 matrix
    board = [['.'] * 3] * 3

    
    return board

def print_board(board):
    print(board) # DEBUG

def end():
    pass

def reset():
    pass

# Start game
game()