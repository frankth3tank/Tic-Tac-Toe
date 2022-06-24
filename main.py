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
        
def player_play(board, character, location_row, location_col):
    board[location_row][location_col] = character
    
def position_row():
    location_row = int(input("What row would you like to play?: "))
    
    if location_row < 0 or location_row > 2:
        print("Please Enter a number between 0 and 2")
        position_row()
    else:
        return location_row
    
def position_col():
    location_col = int(input("What column would you like to play?: "))
    
    if location_col < 0 or location_col > 2:
        print("Please Enter a number between 0 and 2")
        position_col()
    else:
        return location_col
    
    
        
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

location_row = position_row()
location_col = position_col()

player_play(board, player_character, location_row, location_col)

show_board(board)



    
