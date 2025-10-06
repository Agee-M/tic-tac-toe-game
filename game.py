import random

def game():
    # First game
    playing = False

    # Initialize game
    if not playing:
        game_board, selection_board, players = start()
    playing = True 

    # Game loop
    valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while playing:
        playing = play(game_board, selection_board, players, valid)
        
        # Game finished
        if not playing:
            while True:
                choice = input("Do you want to play again? (Y/N): ").upper()
                
                # Reset game
                if choice.startswith("Y"):
                    playing, valid, game_board, selection_board = reset(players)
                    break
                else:
                    print("Game Over")
                    return
    return

def play(game_board, selection_board, players, valid): 
    # Game state
    playing = True
    
    # Helper variables
    match = {'7': (0, 0), '8':(0, 1), '9': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '1': (2, 0), '2': (2, 1), '3': (2, 2)}
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
    player = ""
    
    # Make choice
    while True:
        # Helper board
        print_board(game_board, selection_board, is_select = True)
        # Main board
        print_board(game_board, selection_board, is_select = False)


        # Check current player
        if players["Player1"]["Turn"] == True:
            choice = input(f"{players["Player1"]["Name"]} select a spot: ")
            print()
            player = "Player1"
        else:
            # Check if non-player
            if players["Player2"]["CP"] == True:
                while True:
                    
                    # Generate random valid choice
                    choice = str(random.randrange(1, 10))
                    if choice in valid:
                        break

            # Human player 2
            else:
                choice = input(f"{players["Player2"]["Name"]} select a spot: ")
            player = "Player2"
        
        # Validate spot is open
        if choice in valid:
            break
        elif len(valid) == 0:
            break
        else:
            print()
            print("Invalid: Choose an empty spot")
            print()

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
    for i, val in enumerate(win):
        
        # Win conditions met
        if set(players[player]["Placements"]) >= val:
            print(f"{players[player]["Name"]} WINS!!!")
            print()
            playing = False
            return playing
        
        # No win conditions met - No spaces left
        elif len(valid) == 0 and i == len(win) - 1:
            print("It's a tie!")
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
    print("Welcome to Tic-Tac-Toe!")
    print()
    
    # Initialize new boards
    board1, board2 = new_boards()

    # Initialize players
    players = new_players()

    # Return to game
    return board1, board2, players

def new_players():
    # Initialize players dict
    players = {
        "Player1": {"Name": "", "Symbol": "", "Turn": None, "Placements": ''},
        "Player2": {"Name": "", "Symbol": "", "Turn": None, "Placements": '', "CP": None}
    }

    # print("DEBUG - Players init")
    # print(players)

    # Assign player1 name
    players["Player1"]["Name"] = input("Player 1 (name): ")
    print()
    
    
    # Validate choice character
    valid = ("X", "O")
    while True:

        # Assign player 1 symbol
        choice = input("Pick X or O: ").upper()
        print()
        if choice not in valid:
            print("Invalid choice")
        else:
            print(f"{players["Player1"]["Name"]} is {choice}")
            print()
            players["Player1"]["Symbol"] = choice
            break

    # Single player or multiplayer
    while True:
        single = input("Is this single player? (Y/N): ").upper()
        print()
        if single.startswith("Y"):
            players["Player2"]["CP"] = True
            break
        else:
            break
    
    # Assign player 2 name
    if players["Player2"]["CP"] == True:
        players["Player2"]["Name"] = "Khaleesi_AI"
    else:
        players["Player2"]["Name"] = input("Player 2 (name): ")

    # Assign player 2 symbol
    if choice == "X":
        players["Player2"]["Symbol"] = "O"
    else:
        players["Player2"]["Symbol"] = "X"
    print(f"{players["Player2"]["Name"]} is {players["Player2"]["Symbol"]}")
    print()

    # print("DEBUG - Players choice")
    # print(players)

    # Determine first and second player
    key = ['1', '2']
    while True:
        first = input("Who will start? (1/2): ")
        print()
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

def new_boards():
    # Creates 3 x 3 matrix
    board1 = [['.'] * 3 for _ in range(3)]
    board2 = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
    
    # Return to start
    return board1, board2

def print_board(board, selections, is_select):
    # Format board
    if not is_select:

        # Current game board
        print("Choose a spot: ", end='\n\n')
        for row1 in board[:1]:
            print("   ".join(row1), end='\n\n')
        for row2 in board[1:2]:
            print("   ".join(row2), end='\n\n')
        for row3 in board[2:]:
            print("   ".join(row3), end='\n\n')
    else:     
        
        # Helper board (show available choices with numbers)
        print("(Help) ", end='\n\n')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '.':
                    print(selections[i][j] + "   ", end='')
                else:
                    print("[" + board[i][j].lower() + "]" + "   ", end='')
            print(end='\n\n')

def reset(players):
    # Reset game with names intact
    valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    players["Player1"]["Placements"] = ''
    players["Player2"]["Placements"] = ''
    playing = True
    board1, board2 = new_boards()
    return playing, valid, board1, board2

# Start game
game()


# DEBUG