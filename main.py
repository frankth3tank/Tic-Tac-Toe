import random

def welcome_player(name):
    print(f"Welcome {name} to Tic-Tac-Toe!")
    
def player_choose_character():
    choice = input("What character would you be playing with 'X' or 'O': ")
    if choice.upper() == "X":
        return "X"
    elif choice.upper() == "O":
        return "O"

    
player_choice = player_choose_character()
print(player_choice)
    
