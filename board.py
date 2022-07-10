class Board:
    
    def __init__(self):
        self.board = []
        for index in range(9):
            self.board.append(index + 1)
     
    def show_board(self):
        steps = 2
        for index in range(len(self.board)):
            if index > 0 and index % steps == 0:
                print(self.board[index], end="\n")
                steps += 3
            else:
                print(self.board[index], end=" ")
        
    def play(self, character, choice):
        self.board[choice - 1] = character