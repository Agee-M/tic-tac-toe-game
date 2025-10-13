import random

# Game, Board, Players, Debug

class Board():

    # Initial board
    def __init__(self, board_size: int = 3):    
        if board_size < 3:
            board_size = 3
        self.board = [["."] * board_size for i in range(board_size)]

    # Validate move on board
    def is_valid(self, choice: list[int, int]) -> bool:
        if self.board[choice[0]][choice[1]] == '.':
            return True
        return False
            
    # Make move
    def make_move(self, choice: list[int, int], symbol: str):

        # Check for invalid move     
        if not self.is_valid(choice):
            print("Invalid choice")
            print()
            return 
        
        # Update board
        self.update_board(choice, symbol)

    # Update board
    def update_board(self, choice: list[int, int], symbol: str):
        self.board[choice[0]][choice[1]] = symbol
        
    # Check tie
    def is_tie(self) -> bool:
        if self.valid == []:
            return True
        return False

    # Check win
    def is_win(self, symbol: str) -> bool:
        size = len(self.board)
        
        # Check rows
        win = True
        for r in range(size):
            for c in range(size):
                if self.board[r][c] == symbol:
                    pass
                else:
                    win = False
                    break

        # Row win condition met
        if win:
            return True
    
        # Check columns
        win = True
        for c in range(size):
            for r in range(size):
                if self.board[r][c] == symbol:
                    pass
                else:
                    win = False
                    break

        # Column win condition met
        if win:
            return True
    
        # Diagonal Algorithms   
        # Check \
        win = True
        for r in range(size):
            if self.board[r] == self.board[c] == symbol:
                pass
            else:
                win = False
            if not win:
                break

        # Diagonal 1 win condition met
        if win:
            return True
        
        # Check /
        win = True
        row_ind = 0
        col_ind = size - 1
        for _ in range(size):
            if self.board[row_ind] == self.board[col_ind] == symbol:
                row_ind += 1
                col_ind -= 1
                pass
            else:
                win = False
                break
        
        # Diagonal 2 win condition met
        if win:
            return True

        return False

    # Print board
    def print_board(self):
        print(self.board)

class Player():
    
    def __init__(self):
        self.name = ''
        self.symbol = ''
        self.is_turn = None
        self.is_human = True

    # Set computer player (single player)
    def set_computer(self):
        self.name = 'Khaleesi_AI'
        self.is_human = False

class Game():

    # Initialize a board, game, and 2 players

    def __init__(self):
        self.game_board = Board()
        self.board_positions = {}
        self.player1 = Player(1)
        self.player2 = Player(2)

        self.init_board_positions() 

    # Initialize board positions for game
    def init_board_positions(self):
        size = len(self.game_board.board)
        self.board_positions = {}
        row_ind = 0
        col_ind = 0
        for i in range(1, (size * size) + 1):   
            matrix = [row_ind, col_ind]
            self.board_positions[str(i)] = matrix
            if i % size == 0:
                row_ind += 1
                col_ind = 0
            else:
                col_ind += 1

    # Generate computer move
    def random_move(self) -> int:
        while True:

            # BUG: Possible issue with randrange and what is_valid() accepts
            # Check if is_valid accepts 0-9 or 1-10
            choice = str(random.randrange(1, len(self.board) * len(self.board) + 1))
            if self.game_board.is_valid(choice):
                return choice
            

    # Converts choice to board coordinates
    def choice_to_board(self, choice: str) -> dict[int, int]:
        return self.board_positions[choice]
    
    # Reset game
    def reset(self):
        self.board = Board()

    # Swap players
    def swap_turns(self):
        self.player1.is_turn = False if self.player1.is_turn else True
        self.player2.is_turn = False if self.player2.is_turn else True
        

    # Set up players
    def player_setup(self):

        print("Welcome to tic-tac-toe!")
        print()
        
        # Prompt for 1 or 2 players (game-mode)
        while True:
            ans = input("Is there only 1 player? (Y/N): ").upper()
            print()
            if ans.startswith('Y'):
                self.player2.set_computer()
            break

        # Set names
        self.player1.name = input("Player 1 (name): ")
        print()
        if self.player2.is_human:
            self.player2.name = input("Player 2 (name): ")
            print()

        # Set symbols
        while True:
            ans = input(f"{self.player1.name} - X or O? (X/O): ").upper()
            print()
            if ans == 'X' or ans == 'O':
                self.player1.symbol = ans
                break
            else:
                print("Choose X or O")
                print()

        # Choose turn
        while True:
            ans = input(f"Does {self.player1.name}(1) or {self.player2.name}(2) go first? (1/2): ")
            print()
            if ans == '1':
                self.player1.is_turn = True
                self.player2.is_turn = False
                break
            elif ans == '2':
                self.player1.is_turn = False
                self.player2.is_turn = True
                break
            else:
                print("Type 1 or 2")
    
    # Set up board
    def board_setup(self):
        while True:
            try:
                size = input("Choose a board size: ")
            except ValueError:
                print("Give a number")
            else:
                break

    # Make a play
    def play_turns(self, curr_player: object, next_player: object):
        
        # BUG: make_move() accepts list[int, int], not str

        # First player
        if curr_player.is_human:
            choice = input(f"{curr_player.name} pick an option (1-{len(self.board)}): ")
        else:
            choice = self.random_move()
        self.board.make_move(choice, curr_player.symbol)

        # Print board
        self.game_board.print_board()

        # Second player
        if next_player.is_human:
            choice = input(f"{next_player.name} pick an option (1-{len(self.board)}): ")
        else:
            choice = self.random_move()
        self.board.make_move(choice, next_player.symbol)

        # Print board
        self.game_board.print_board()

    # Run game
    def run(self):

        print("Game start!")
        print()

        if self.player1.is_turn:
            self.play_turns(self.player1, self.player2)
        else:
            self.play_turns(self.player2, self.player1)
        
        # Swap turns
        self.swap_turns()

# TODO: Finish AI implementation
# TODO: Fix bug with choice
# TODO: Check whether passing obj works
# TODO: Implement game loop
# TODO: Implement reset
# TODO: Test
# TODO: Implement unit testing
