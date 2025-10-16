import random

class Board():

    # Initial board
    def __init__(self, board_size: int = 3):    
        if board_size < 3:
            board_size = 3
        elif board_size > 10:
            board_size = 10
        self.board = [["."] * board_size for i in range(board_size)]

    # Validate move on board
    def is_valid(self, choice: list[int, int]) -> bool:
        if self.board[choice[0]][choice[1]] == '.':
            return True
        return False
            
    # Make move
    def make_move(self, choice: list[int, int], symbol: str):
        self.board[choice[0]][choice[1]] = symbol   
        
    # Check tie
    def is_tie(self) -> bool:
        size = len(self.board)
        for row in range(size):
            for col in range(size):
                if self.board[row][col] == '.':
                    return False
        return True

    # Check win
    def is_win(self, symbol: str) -> bool:
        size = len(self.board)
        
        # Check rows
        win = True
        r = c = 0
        for r in range(size):
            for c in range(size):
                if self.board[r][c] == symbol:
                    win = True
                    pass
                else:
                    win = False
                    break
            # Row win condition met
            if win:
                return True
    
        # Check columns
        win = True
        r = c = 0
        for c in range(size):
            for r in range(size):
                if self.board[r][c] == symbol:
                    win = True
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
        for i in range(size):
            if self.board[i][i] == symbol:
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
        r = 0
        c = size - 1
        for _ in range(size):
            if self.board[r][c] == symbol:
                r += 1
                c -= 1
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
        for i in range(len(self.board)):
            for row in self.board[i]:
                print("".join(row), end='   ')
            print()
            print()
        print()

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
        self.game_board = None
        self.board_positions = {}
        self.player1 = Player()
        self.player2 = Player()
        self.round = 0
        self.board_size = 0


    # Initialize board positions for game
    def init_board_map(self):
        """game_board.board[0][total squares], but board positions maps it
        in a human readable way, '1' = (0, 0). When interfacing with board.positions,
        make sure to shift the iteration by 1. Ex; 3x3 board has size of 9 ->
        for _ in range(1, 10)"""

        size = len(self.game_board.board)
        self.board_positions = {}
        r = 0
        c = 0
        for i in range(1, (size * size) + 1):   
            matrix = [r, c]
            self.board_positions[str(i)] = matrix
            if i % size == 0:
                r += 1
                c = 0
            else:
                c += 1

    # Generate computer move
    def random_move(self) -> int:
        while True:
            choice = str(random.randrange(1, len(self.game_board.board) * len(self.game_board.board) + 1))
            choice = self.choice_to_board(choice)
            if self.game_board.is_valid(choice):
                return choice
            

    # Converts choice to board coordinates
    def choice_to_board(self, choice: str) -> list[int, int]:
        return self.board_positions[choice]
    
    # Reset game
    def reset(self, board_size: int):
        self.round += 1
        self.game_board = Board(board_size)
        self.run(self.round)

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
            if ans == 'X':
                self.player1.symbol = ans
                self.player2.symbol = 'O'
                break
            elif ans == 'O':
                self.player1.symbol = ans
                self.player2.symbol = 'X'
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
        
        # Choose board size
        while True:
            try:
                self.board_size = int(input("Choose a board size: "))
            except ValueError:
                print("Give a number")
            else:
                break
        
        # Set up game board
        self.game_board = Board(self.board_size)

        # Set board map
        self.init_board_map()

    # Get player move
    def get_move(self, name: str) -> str:
        while True:
            try:
                choice = int(input(f"{name} pick an option (1-{len(self.game_board.board) * len(self.game_board.board)}): "))
                print()
            except ValueError:
                print("Input number")
                print()
            else:
                break
        return str(choice)
    
    # Validate move input
    def is_between(self, choice: str) -> bool:
        return 0 < int(choice) <= len(self.game_board.board) * len(self.game_board.board)

    # Make a play
    def play_turns(self, curr_player: object):
        
        # AI move
        if not curr_player.is_human:
            choice = self.random_move()
            self.game_board.make_move(choice, curr_player.symbol)
            return
        
        while True:
            
            # Get move
            choice = self.get_move(curr_player.name)

            # Validate input    
            if not self.is_between(choice):
                print("Invalid number")
                print()
                continue

            # Convert choice
            choice = self.choice_to_board(str(choice))

            # Validate board
            if self.game_board.is_valid(choice):
                break
            else:
                print("Pick an empty spot!")
                print()
                self.game_board.print_board()
       
        # Update board
        self.game_board.make_move(choice, curr_player.symbol)

        # Print board
        self.game_board.print_board()

    # Run game
    def run(self, round: int = 0):
        
        # Game setup
        if round == 0:
            self.player_setup()
            self.board_setup()

        print("Game start!")
        print()

        # Print default board
        self.game_board.print_board()

        # Game loop
        while True:
            current_player = ""
            current_symbol = ""

            # Make turn
            if self.player1.is_turn:
                self.play_turns(self.player1)
                current_player = self.player1.name
                current_symbol = self.player1.symbol
            else:
                self.play_turns(self.player2)
                current_player = self.player2.name
                current_symbol = self.player2.symbol

            # Check for win
            if self.game_board.is_win(current_symbol):
                print(f"{current_player} won!")
                print()
                break

            # Check for tie
            if self.game_board.is_tie():
                print("It's a tie!")
                print()
                break

            # Swap turns
            self.swap_turns()

        # Prompt for reset
        while True:
            ans = input("Do you want to play again? (Y/N): ").upper()
            if ans.startswith("Y"):
                self.reset(self.board_size)
            else:
                break

        # End
        print("End game")
        print()

class Debug:
    # Classes
    def __init__(self):
        self.game_d = Game()
        self.board_d = Board()
        self.player1_d = Player()
        self.player2_d = Player()
    
    # Test run script
    def play_test(self):
        pass

    # Win conditions
    def win(self):
        self.game_d.board_setup()
        print(self.board_d.is_win('x'))

if __name__ == "__main__":
    game = Game()
    game.run()