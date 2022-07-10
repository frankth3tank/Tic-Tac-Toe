import random
class Player:
    
    def __init__(self, name):
        self.name = name
    
    def welcome_player(self):
        print(f"Welcome {self.name} to Tic-Tac-Toe!")
        
    def player_choose_character(self):
        choice = input("What character would you be playing with 'X' or 'O': ").upper()
        if choice == "X" or choice == "O":
            return choice
        else:
            print("Invalid Character, choose between 'X' or 'O'")
            return self.player_choose_character()
        
    def player_choice(self):
        choice = int(input("What position would you like to play?: "))
        if choice < 0 or choice > 9:
            print("Please Enter a number between 1 and 9")
            return self.player_choice()
        else:
            return choice 
    
    def cpu_character(self, player_character):
        if player_character == "X":
            return "O"
        elif player_character == "O":
            return "X"
        
    def cpu_choice(self):
        comp_choice = random.randint(1, 9)
        return comp_choice
        
    
            
    