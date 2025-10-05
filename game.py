# TODO: Tic-tac-toe game implementation

def game():
    # Initialize game
    game_board, selection_board, players, is_select = start()

    # Interactivity
    if players["Player1"]["Turn"] == True:
        input(f"{players["Player1"]["Name"]} select a spot: ")
        players["Player1"]["Turn"] = False
        players["Player1"]["Turn"] = True

    else:
        input(f"{players["Player2"]["Name"]} select a spot: ")
        players["Player1"]["Turn"] = True
        players["Player1"]["Turn"] = False


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
    # TODO: Make 1 player or 2 player


    return


def start():
    print("New Game")
    
    # Initialize new boards
    board1, board2 = new_boards()

    # Set selection state
    state = False

    # Initialize players
    players = new_players()

    # Return to game
    return board1, board2, players, state

def new_players():
    # Initialize players dict
    players = {
        "Player1": {"Name": "", "Choice": "", "Turn": None, "Score": 0},
        "Player2": {"Name": "", "Choice": "", "Turn": None, "Score": 0}
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
            players["Player1"]["Choice"] = choice
            break
    
    # Assign player 2 name and choice
    players["Player2"]["Name"] = input("Player 2: ")
    if choice == "X":
        players["Player2"]["Choice"] = "O"
    else:
        players["Player2"]["Choice"] = "X"
    print(f"{players["Player2"]["Name"]} is {players["Player2"]["Choice"]}")

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
    print(players["Player1"]["Name"])
    print(players["Player2"]["Name"])

def end():
    pass

def reset():
    pass

# Start game
game()


# DEBUG
    


