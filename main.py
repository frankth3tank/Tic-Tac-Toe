import random

def welcome_player(name):
    print(f"Welcome {name} to Tic-Tac-Toe!")
    
def player_choose_character():
    choice = input("What character would you be playing with 'X' or 'O': ")
    if choice.upper() == "X":
        return "X"
    elif choice.upper() == "O":
        return "O"
    else:
        print("Invalid Character, choose between 'X' or 'O'")
        return player_choose_character()
    
def show_board(board):
    steps = 2
    for index in range(len(board)):
        if index > 0 and index % steps == 0:
            print(board[index], end="\n")
            steps += 3
        else:
            print(board[index], end=" ")
        
def play(board, character, choice):
    board[choice - 1] = character
    
def player_choice():
    choice = int(input("What position would you like to play?: "))
    if choice < 0 or choice > 9:
        print("Please Enter a number between 1 and 9")
        return player_choice()
    else:
        return choice  
    
def comp_character(player_character):
    if player_character == "X":
        return "O"
    elif player_character == "O":
        return "X"
    
def comp_choice():
    comp_choice = random.randint(1, 9)
    return comp_choice

def is_board_full(board):
    count = 0
    for item in board:
        if item == "O" or item == "X":
            count += 1
        else:
            count = count
    if count >= 9:
        return True
    else: 
        return False
    
def ending_condition(board, character, player):
    if board[0] == character and board[1] == character and board[2] == character:
        print(f"{player} Won!!")
        return True
    elif board[3] == character and board[4] == character and board[5] == character:
        print(f"{player} Won!")
        return True
    elif board[6] == character and board[7] == character and board[8] == character:
        print(f"{player} Won!")
        return True
    elif board[0] == character and board[3] == character and board[6] == character:
        print(f"{player} Won!")
        return True
    elif board[1] == character and board[4] == character and board[7] == character:
        print(f"{player} Won!")
        return True
    elif board[2] == character and board[5] == character and board[8] == character:
        print(f"{player} Won!")
        return True
    elif board[0] == character and board[4] == character and board[8] == character:
        print(f"{player} Won!")
        return True
    elif board[2] == character and board[4] == character and board[6] == character:
        print(f"{player} Won!")
        return True
        
    
    
board = []

for index in range(9):
    board.append(index + 1)
    
is_game_over = False

player_name = input("What is your name?: ")
welcome_player(player_name)
print("-------------------------------------------------")
player_character = player_choose_character()
print("-------------------------------------------------")

while is_game_over == False:
    show_board(board)
    print("-------------------------------------------------")
    
    players_turn =  True
    player_choice_position = player_choice()

    while players_turn:
        if board[player_choice_position - 1] == "X" or board[player_choice_position - 1] == "O":
            print("Postion already occupied")
            player_choice_position = player_choice()
        else:
            play(board, player_character, player_choice_position)
            players_turn = False
            if ending_condition(board, player_character, player_name):
                is_game_over = True
            else:
                pass

    show_board(board)
    print("-------------------------------------------------")
    
    cpu_turn = True
    cpu_character = comp_character(player_character)
    cpu_choice_position = comp_choice()
    
    while cpu_turn:
        if board[cpu_choice_position - 1] == "X" or board[cpu_choice_position - 1] == "O":
            cpu_choice_position = comp_choice()
        else:
            play(board, cpu_character, cpu_choice_position)
            cpu_turn = False
            if ending_condition(board, cpu_character, "CPU"):
                is_game_over = True
            else:
                pass
    
    if is_board_full(board):
        print("Is a Draw!")
        is_game_over = True
