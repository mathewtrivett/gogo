class Board:
    def __init__(self,size):
        self.size = size
        self.matrix = [[None for x in range(self.size)] for y in range(self.size)]
        self.groups = []

    def offBoard(self,coordinates):
        offBoard = False
        for (coordinate) in coordinates:
            if coordinate > self.size or coordinate < 0:
                offBoard = True
        return offBoard
