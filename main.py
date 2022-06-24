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
    steps = 2
    for index in range(len(board)):
        if index > 0 and index % steps == 0:
            print(board[index], end="\n")
            steps += 3
        else:
            print(board[index], end=" ")
        
def player_play(board, character, choice):
    board[choice - 1] = character
    
def player_choice():
    choice = int(input("What position would you like to play?: "))
    if choice < 0 or choice > 9:
        print("Please Enter a number between 0 and 2")
        player_choice()
    else:
        return choice  
    
board = []

for index in range(9):
    board.append(index + 1)

    
player_name = input("What is your name?: ")
welcome_player(player_name)

player_character = player_choose_character()

show_board(board)

player_choice_position = player_choice()


player_play(board, player_character, player_choice_position)

show_board(board)



    
