import random

# Game, Board, Players, Debug

class Board():

    # Initial board
    def __init__(self, board_size: int = 3):    
        if board_size < 3:
            board_size = 3
        self.board = [["."] * board_size for i in range(board_size)]
        self.valid_moves = [i for i in range(1, (board_size * board_size) + 1)]

    # Spot validator
    def is_valid(self, choice: int) -> bool:
        if choice in self.valid:
            return True
        return False
    
    # Valid updater
    def update_valid(self, choice: int):
        for i, val in enumerate(self.valid):
            if val == choice:
                self.valid.pop(i)
                return
            
    # Make move
    def make_move(self, choice: int, symbol: str):

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
    def check_win(self, symbol: str) -> bool:
        size = len(self.board)
        # Check rows
        win = True
        for r in range(size):
            for c in range(size):
                if self.board[r][c] == self.board[r][c] == symbol:
                    pass
                else:
                    win = False
            # TODO: Fix iterations
            
       
            
        # Check columns
        for c in range(size):
            if self.board[0][c] == self.board[1][c] == self.board[2][c] == symbol:
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

        # Win condition met
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

        # Win condition met
        return win

    # Print board
    def print_board(self):
        print(self.board)

class Player():
    
    def __init__(self):
        self.player = 0
        self.name = ''
        self.symbol = ''
        self.turn = None
        self.human = True

    # Single player
    def set_computer(self):
        self.name = 'Khaleesi_AI'
        self.human = False

class Game():

    # Initialize a board, game, and 2 players

    def __init__(self):
        self.game_board = Board()
        self.player1 = Player()
        self.player2 = Player()

    # Generate computer move
    def random_move(self) -> int:
        while True:
            choice = str(random.randrange(1, 10))
            if choice in self.valid:
                return choice

    # Convert board size to position_conv dict
    def board_to_choice(self) -> dict[int, int]:
        size = len(self.game_board.board)
        position_conv = {}
        row_ind = 0
        col_ind = 0
        for i in range(1, (size * size) + 1):   
            matrix = [row_ind, col_ind]
            position_conv[str(i)] = matrix
            if i % size == 0:
                row_ind += 1
                col_ind = 0
            else:
                col_ind += 1
        return position_conv
    
    def choice_to_board(self, choice: str, position_conv: dict[int, int]) -> list[int, int]:
        return position_conv[choice]

    # Ask for user input

    # Return tuple of selection location 



# class Debug():

#     # Test board initialization
#     def __init__(self) -> object:
#         self.debug = Board()

#     # Test board print    
#     def board(self):
#         debug.print_board()


# DEBUG
x = Board()

x.print_board()