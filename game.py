# TODO: Tic-tac-toe game implementation

def game():
    # Initialize game
    # game_board, selection_board, players, is_select = start()
    game_board, selection_board = new_boards()
    # is_select = False
    game_board[2][2] = 'X'
    game_board[0][2] = 'O'
    game_board[1][1] = 'X'
    game_board[2][0] = 'X'
    
    # DEBUG
    print_board(game_board, selection_board, is_select = False)
    print()
    print_board(game_board, selection_board, is_select = True)
    #print_players(players)


    

    # Show positions as matrix (1 - 9) 
    # Combine game board with choice board (or just remove dots for choice board)
    # TODO: Add interactivity between choices and board
    # TODO: Add win conditions (including tie)
    # TODO: Add reset functionality
    # TODO: Add winner goes first?


    return


def start():
    print("New Game")
    
    # Initialize new boards
    board1, board2 = new_boards()

    # Initialize players
    players = new_players()

    # Set game state
    state = False

    # Return to game
    return board1, board2, players, state

def new_players():
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

    # Return to start
    return players


def score():
    pass

def new_boards():
    # Creates 3 x 3 matrix
    board1 = [['.'] * 3 for _ in range(3)]
    board2 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    
    # Return to start
    return board1, board2

def print_board(board, selections, is_select):
    # Format board
    if not is_select:
        # Current game board
        print("Current: ", end='\n\n')
        for row1 in board[:1]:
            print("   ".join(row1), end='\n\n')
        for row2 in board[1:2]:
            print("   ".join(row2), end='\n\n')
        for row3 in board[2:]:
            print("   ".join(row3), end='\n\n')
    else:     
        # Available selection options
        print("Selection: ", end='\n\n')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    print(selections[i][j] + "   ", end='')
                else:
                    print("[" + board[i][j].lower() + "]" + "   ", end='')
            print(end='\n\n')

def print_players(players): # DEBUG
    # {Player#: [Name, Choice (X or O)]}
    print(players["Player1"][0])
    print(players["Player2"][0])

def end():
    pass

def reset():
    pass

# Start game
game()
