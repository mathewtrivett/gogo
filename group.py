class Group:
    
    def __init__(self, colour, coordinates):
        self.coordinates = set()
        self.colour = colour
        self.coordinates = self.coordinates.union(coordinates)
        
    '''
    Merges group into self, then telling the board to delete the reference to group,
    '''
    def mergeGroup(self, group, board):
        self.coordinates = self.coordinates.union(group.coordinates)
        board.deleteGroup(group)

    '''
    Checks is a given coordinate belongs to the group
    '''
    def isInGroup(self, testCoord):
        for groupCoord in self.coordinates:
            if groupCoord == testCoord:
                return True
        return False
    
    '''
    Checks if there is an empty square touching the group, if not then is it
    captured and the function returns true
    '''
    def isCaptured(self, board):
        for coord in self.coordinates:
            for neighbour in board.neighbours(coord):
                if self.isInGroup(neighbour) : # we must include this check so that the function can deal with virtual groups
                    continue
                elif board.getGroup(neighbour).colour == 'None': #any empty square touching the group indicates it is not captured
                    return False
        return True

from board import Board
