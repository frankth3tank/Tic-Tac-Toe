class Board:
    
    def __init__(self, sizeX=3, sizeY=3):
        self.board = []
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.size = sizeX * sizeY
        for index in range(self.size):
            self.board.append(index + 1)
     
    def show_board(self):
        col = 0
        for index in range(len(self.board)):
            if col > 0 and col % 2 == 0:
                print(self.board[index], end="\n")
                col = 0
            else:
                print(self.board[index], end=" ")
                col += 1
        
    # def play(self, character, choice):
    #     self.board[choice - 1] = character  #board.board[choice - 1]
