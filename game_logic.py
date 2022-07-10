class GameLogic:
    
    def __init__(self):
        pass
        
    def ending_condition(self, board, character, player):
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
    
    def is_board_full(self, board):
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