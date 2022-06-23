import random

def welcome_player(name):
    print(f"Welcome {name} to Tic-Tac-Toe!")
    
def player_choose_character():
    choice = input("What character would you be playing with 'X' or 'O': ")
    if choice.upper() == "X":
        return "X"
    elif choice.upper() == "O":
        return "O"
    
def show_board(board):
    for row in board:
        for item in row:
            print(item, end=" ")
        print()
        
board = []

for _ in range(3):
    row = []
    for _ in range(3):
        row.append("-")
    board.append(row)

    
