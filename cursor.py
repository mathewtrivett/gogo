class Cursor:
    
    def __init__(self, board):
        self.board = board
        self.coordinates = (0,0)
        
    def moveTo(self,newPos):
        if self.board.offBoard(newPos):
            return False
        else:
            self.coordinates = newPos
            return True
        
    def moveBy(self,change):
        newPos = tuple(map(lambda x, y: x+y, self.coordinates, change))
        return self.moveTo(newPos)
