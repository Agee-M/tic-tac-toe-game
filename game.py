# TODO: Tic-tac-toe game implementation

def game():
    # First game
    playing = False

    # Initialize game
    if not playing:
        game_board, selection_board, players = start()
    playing = True 

    # Game loop
    while playing:
        playing = play(game_board, selection_board, players)

        # Playing will return false when game is done
        # TODO: Ask for playing again
    

    # Show positions as matrix (1 - 9) 
    # Combine game board with choice board (or just remove dots for choice board)
    # Add interactivity between choices and board
    # Add win conditions (including tie)
    # TODO: Add reset functionality
    # TODO: Add winner goes first?
    # TODO: Make 1 player or 2 player

    print("EOF")
    return

def play(game_board, selection_board, players): 
    # Game state
    playing = True
    
    # Helper variables
    valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    match = {'1': (0, 0), '2':(0, 1), '3': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (2, 0), '8': (2, 1), '9': (2, 2)}
    win = [
        {'1', '2', '3'},
        {'4', '5', '6'},
        {'7', '8', '9'},
        {'1', '4', '7'},
        {'2', '5', '8'},
        {'3', '6', '9'},
        {'1', '5', '9'},
        {'3', '5', '7'}
    ]
    symbol_x = {}
    symbol_y = {}
    player = ""
    
    # Make choice
    while True:

        # Choose a spot
        if players["Player1"]["Turn"] == True:
            choice = input(f"{players["Player1"]["Name"]} select a spot: ")
            player = "Player1"
        else:
            choice = input(f"{players["Player2"]["Name"]} select a spot: ")
            player = "Player2"
        
        # Validate spot is open
        if choice in valid:
            break
        else:
            print("Choose an empty spot")

    # Change player turns
    swap(players)

    # Track placements on board
    print(choice)
    players[player]["Placements"] += choice

    # Add X or O inside of game_board
    game_board[match[choice][0]][match[choice][1]] = players[player]["Symbol"]
    print_board(game_board, selection_board, is_select = False)

    # Remove option from available choices
    for i, val in enumerate(valid):
        if val == choice:
            valid.pop(i)

    # Check to see if 3 in a row
    for i in win:
        if set(players[player]["Placements"]) >= i:
            print(f"{players[player]["Name"]} WINS!!!")
            playing = False
            return playing
    return playing

def swap(players):
    # Change player turn
    if players["Player1"]["Turn"] == True:
        players["Player1"]["Turn"] = False
        players["Player2"]["Turn"] = True
    else:
        players["Player1"]["Turn"] = True
        players["Player2"]["Turn"] = False

def start():
    print("New Game")
    
    # Initialize new boards
    board1, board2 = new_boards()

    # Initialize players
    players = new_players()

    # Return to game
    return board1, board2, players

def new_players():
    # Initialize players dict
    players = {
        "Player1": {"Name": "", "Symbol": "", "Turn": None, "Score": 0, "Placements": ''},
        "Player2": {"Name": "", "Symbol": "", "Turn": None, "Score": 0, "Placements": ''}
    }

    # print("DEBUG - Players init")
    # print(players)

    # Assign player1 name
    players["Player1"]["Name"] = input("Name (Player1): ")
    
    # Validate choice character
    valid = ("X", "O")
    while True:

        # Assign player 1 choice
        choice = input("Pick X or O: ").upper()
        if choice not in valid:
            print("Invalid choice")
        else:
            print(f"{players["Player1"]["Name"]} is {choice}")
            players["Player1"]["Symbol"] = choice
            break
    
    # Assign player 2 name and choice
    players["Player2"]["Name"] = input("Player 2: ")
    if choice == "X":
        players["Player2"]["Symbol"] = "O"
    else:
        players["Player2"]["Symbol"] = "X"
    print(f"{players["Player2"]["Name"]} is {players["Player2"]["Symbol"]}")

    # print("DEBUG - Players choice")
    # print(players)

    # Determine first and second player
    key = ['1', '2']
    while True:
        first = input("Who will start? (1/2): ")
        if first in key:
            
            # Convert position to dict key
            key.pop(int(first) - 1)
            first = "Player" + first
            second = "Player" + key[0]

            # Assign positions
            players[first]["Turn"] = True
            players[second]["Turn"] = False

            # print("DEBUG - Players positions")
            # print(players)
            break
        else:
            print("Type 1 or 2")

    # Return to start
    return players

def score():
    pass

def new_boards():
    # Creates 3 x 3 matrix
    board1 = [['.'] * 3 for _ in range(3)]
    board2 = [['9', '8', '7'], ['6', '5', '4'], ['3', '2', '1']]
    
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
    print(players["Player1"]["Name"])
    print(players["Player2"]["Name"])

def end():
    pass

def reset():
    pass

# Start game
game()


# DEBUG
    
# BUG: Valid doesn't stop from pressing new inputs
# BUG: Valid doesn't have functionality for min/complete removals
# BUG: Input overwrites current position
# TODO: Change names/intro


