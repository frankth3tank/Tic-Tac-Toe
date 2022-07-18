import random
class Player:
    
    def __init__(self, type, name, board):
        self.name = name
        self.type = type
        self.symbol = ""
        self.occupied_spaces = {}
        
        for i in range(board.size):
            self.occupied_spaces[i] = None
        
    
    def welcome_player(self):
        print(f"Welcome {self.name} to Tic-Tac-Toe!")
        
    def choose_character(self):
        choice = input("What character would you be playing with 'X' or 'O': ").upper()
        if choice == "X" or choice == "O":
            self.symbol = choice  # player.choose_character()  => player.symbol
        else:
            print("Invalid Character, choose between 'X' or 'O'")
            return self.player_choose_character()
        
    def play(self, board, choice):
        index = choice-1
        board.board[index] = self.symbol
        self.occupied_spaces[index] = self.symbol #board.board[choice - 1]
        
    def _player_choice(self):
        choice = int(input("What position would you like to play?: "))
        if choice < 0 or choice > 9:
            print("Please Enter a number between 1 and 9")
            return self.player_choice()
        else:
            return choice 
        
    def player_choice(self):
        choice = self._player_choice() if self.type == "Human" else self._cpu_choice()
        return choice
    
    def cpu_character(self, player_character):
        character = "O" if player_character == "X" else "X"
        return character
        
    def _cpu_choice(self):
        comp_choice = random.randint(1, 9)
        return comp_choice
    
    def notified_position_is_occupied(self):
        if self.type == "Human":
            print("Position is already occupied!")
        
    
            
    