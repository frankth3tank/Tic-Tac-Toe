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
        
def player_play(board, character):
    location_row = int(input("What row would you like to play?: "))
    location_col = int(input("What colum would you like to play?: "))
    board[location_row][location_col] = character
    
    
        
board = []

for _ in range(3):
    row = []
    for _ in range(3):
        row.append("-")
    board.append(row)
    
player_name = input("What is your name?: ")
welcome_player(player_name)

player_character = player_choose_character()

show_board(board)

player_play(board, player_character)

show_board(board)



    
