from Board import Board

class Group:
    
    def __init__(self, colour, coordinates, groupId, isVirtual = False):
        self.colour = colour
        self.coordinates = {coordinates}
        self.id = groupID
        self.isVirtual = isVirtual#virtual groups are not on the game board and are used for analysis

    def mergeGroup(self, group, board):
        if(type(group.id) == NoneType):
            return
        self.coordinates = self.coordinates.union(group.coordinates)
        if(not self.isVirtual):#virtual
            board.deleteGroup(group)

    def isInGroup(self, testCoord):
        for groupCoord in coordinates:
            if(groupCoord == testCoord):
                return True
        return False

    def isCaptured(self, board):
        for coord in self.coordinates:
            for neighbour in board.neighbours(coord):
                if(neighbour isInGroup):#we must include this check so that the function can deal with virtual groups
                    continue
                elif board.getGroup(neighbour).colour == 0:#any empty square touching the group indicates it is not captured
                    return False
        return True
