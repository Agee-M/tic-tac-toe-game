# TODO: Tic-tac-toe game implementation

def game():
    start()


def start():
    print("New Game")
    
    # Initialize new board
    board = new_board()
    print_board(board)

    #Initialize players
    player()

def player():
    # Assign player names and characters
    players = {}
    players["Player1"] = [input("Player 1: "), 0]
    
    # Validate character
    while True:
        try:
            players["Player1"][1] = input("Pick X or O: ").upper()
        except ValueError:
            print("Needs to be a letter")
        if "O" not in players:
            print("WHOOPS")
        else:
            print("YAY")
            return
    players["Player2"] = [input("Player 2: "), 0]
    print("You are {}")
    players["Player2"][1] = "O"
    print(players)


def score():
    pass

def new_board():
    # Creates 3 x 3 matrix
    board = [[] * 3] * 3
    return board

def print_board(board):
    print(board)

def end():
    pass

def reset():
    pass

# Start game
game()