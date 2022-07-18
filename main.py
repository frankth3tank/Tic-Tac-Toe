from board import Board
from player import Player
from game_logic import GameLogic

SIZE_X = 3
SIZE_Y = 3
USE_CPU = True

def turn(player, board):
    turn = True
    while turn:
        pass
    

def main():
    is_game_over = False
    board = Board(SIZE_X, SIZE_Y)
    game_logic = GameLogic(board)

    player_1_name = input("Please Enter Player 1 Name: ")
    player_1 = Player("Human", player_1_name, board)
    player_1.welcome_player()

    if (USE_CPU):
        player_2 = Player("CPU", "CPU", board)

    else:
        player_2_name = input("Please Enter Player 2 Name: ")
        player_1 = Player("Human", player_1_name, board)
        player_1.welcome_player()

    cpu = Player("CPU", "CPU", board)
    print("-------------------------------------------------")

    player_1_character = player_1.choose_character()
    print("-------------------------------------------------")

    while is_game_over == False:
        board.show_board()
        print("-------------------------------------------------")
        
        players_turn =  True
        player_choice_position = player_1.player_choice()

        while players_turn:
            if board[player_choice_position - 1] == "X" or board[player_choice_position - 1] == "O":
                print("Postion already occupied")
                player_choice_position = player_1.player_choice()
            else:
                player_1.play(player_1_character, player_choice_position)
                players_turn = False
                if game_logic.ending_condition(board, player_1_character, player_1):
                    is_game_over = True
                else:
                    pass

        board.show_board(board)
        print("-------------------------------------------------")
        
        cpu_turn = True
        cpu_character = cpu.cpu_character(player_1_character)
        cpu_choice_position = cpu.cpu_choice()
        
        while cpu_turn:
            if board[cpu_choice_position - 1] == "X" or board[cpu_choice_position - 1] == "O":
                cpu_choice_position = cpu.cpu_choice()
            else:
                board.play(board, cpu_character, cpu_choice_position)
                cpu_turn = False
                if game_logic.ending_condition(board, cpu_character, "CPU"):
                    is_game_over = True
                else:
                    pass
        
        if game_logic.is_board_full(board):
            print("Is a Draw!")
            is_game_over = True
            
if __name__ == "__main__":
    main()
        
        

