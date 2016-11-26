class Group:
    
    def __init__(self, colour, coordinates, groupId, isVirtual = False):
        self.coordinates = set()
        self.colour = colour
        self.coordinates = self.coordinates.union(coordinates)
        self.id = groupID
        self.isVirtual = isVirtual #virtual groups are not on the game board and are used for analysis

    '''
    Merges group into self, then telling the board to delete the reference to group,
    if self is virtual then the board will remain unaffected
    '''
    def mergeGroup(self, group, board):
        if type(group.id) == NoneType :
            return
        self.coordinates = self.coordinates.union(group.coordinates)
        if not self.isVirtual :#virtual
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
                if neighbour.isInGroup(neighbour) :#we must include this check so that the function can deal with virtual groups
                    continue
                elif board.getGroup(neighbour).colour == 0: #any empty square touching the group indicates it is not captured
                    return False
        return True

from board import Board
