class GameLogic:

    def __init__(self, board):
        self.board = board

    def _check_horizontal(self, spaces):      
        for i in range(0, self.board.size, 3):
            if spaces[i] != None and spaces[i+1] != None and spaces[i+2] != None:
                return True     
        return False

    def _check_vertical(self, spaces):
        for i in range(0, self.board.sizeX):
            if spaces[i] != None and spaces[i+3] != None and spaces[i+6] != None:
                return True
        return False

    def _check_diagnol(self, spaces):
        if spaces[0] != None and spaces[4] != None and spaces[8] != None:
            return True
        if spaces[2] != None and spaces[4] != None and spaces[6] != None:
            return True
        return False


    def check_match_set(self, player):
        spaces = player.occupied_spaces
        if (self._check_horizontal(spaces) or self._check_vertical(spaces) or self._check_diagnol(spaces)):
            print(f"{player.name} Won!!")

    def is_board_full(self):
        count = 0
        for item in self.board:
            if item == "O" or item == "X":
                count += 1
            else:
                count = count
        if count >= 9:
            return True
        else:
            return False
