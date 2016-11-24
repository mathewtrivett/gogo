class Board:
    def __init__(self,size):
        self.size = size
        self.matrix = [[0 for x in range(self.size)] for y in range(self.size)]
        self.groups = []

    def offBoard(self,coordinates):
        offBoard = False
        for (coordinate) in coordinates:
            if(coordinate > self.size-1) or (coordinate < 0):
                offBoard = True
        return offBoard

    def isEmpty(self, coordinates):
        return self.matrix[coordinates[0]][coordinates[1]] == 0

    def neighbours(self, coordinates):
        neighbours = set()
        for i in [(0,-1),(1,0),(0,1),(-1,0)]:
            neighbour = tuple(map(lambda x, y: x+y, coordinates, i))
            if not self.offBoard(neighbour):
                neighbours.add(neighbour)
        return neighbours

    def isSuicide(self,coordinates,colour):
        group = Group(coordinates, colour, isVirtual=True)
        for neighbour in self.neighbours(coordinates):
            if(neighbour.getGroup(coordinates).colour == group.colour):
                pass
        pass
        # If encounters same colour stone
        # Merge group
        # Return is captured? on merged group

    def getGroup(self, coordinates):
        for group in self.groups:
            for coordinate in group.coordinates:
                if(coordinates == coordinate):
                    return group.id, group.colour
        return None, 0
                    
    def isPlayable(self, coordinates):
        pass
        
    def addGroup(self, group):
        self.groups = self.groups + [group]

    def deleteGroup(self, group):
        pass
