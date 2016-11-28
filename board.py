class Board:
    def __init__(self,size):
        self.size = size
        self.groups = []

    def __str__(self):
        state = ""
        for row in self.getMatrix():
            for col in row:
                if col == 'None':
                    state += "- "
                else:
                    state += col + " "
            state += "\n"
        return state

    '''
    A funtion which mutates one board into another
    '''

    def setTo(self, newBoard):
        self.size = newBoard.size
        self.groups = newBoard.groups
        
    '''
    Returns a matrix representing the current state of the board
    '''
    
    def getMatrix(self):
        matrix = [['None' for x in range(self.size)] for y in range(self.size)]
        for group in self.groups:
            for (x,y) in group.coordinates:
                matrix[y][x] = group.colour
        return matrix

    '''
    Returns a boolean specifing if the position is outside the confines of the board
    '''

    def offBoard(self,coordinates):
        offBoard = False
        for (coordinate) in coordinates:
            if coordinate > self.size-1  or coordinate < 0:
                offBoard = True
        return offBoard

    '''
    Checks if a specific spot on the board contains a stone
    '''

    def isEmpty(self, coordinates):
        return self.getMatrix()[coordinates[1]][coordinates[0]] == 'None'

    '''
    Neighbours looks at coordinates N, S, E and W of a given coordinate.
    If it is not off the board it adds the coordinate to a set and returns the set.
    '''

    def neighbours(self, coordinates):
        neighbours = set()
        for i in [(0,-1),(1,0),(0,1),(-1,0)]:
            neighbour = tuple(map(lambda x, y: x+y, coordinates, i))
            if not self.offBoard(neighbour):
                neighbours.add(neighbour)
        return neighbours

    '''
    isSuicide takes a coordinate and a colour.
    Creates a virtual group then checks all neighbours of the group
    If it finds one with the same colour as itself, it merges that group
    Then it checks if the group is captured, if true, then it is suicide.
    '''

    def isSuicide(self,coordinates,colour):
        group = Group(colour,{coordinates})
        potentialBoard = deepcopy(self)
        potentialBoard.addToGroups(group)
        #first we add any neighbouring allies to the group
        for neighbour in potentialBoard.neighbours(coordinates):
            if potentialBoard.getGroup(neighbour).colour == group.colour:
                group.mergeGroup(potentialBoard.getGroup(neighbour),potentialBoard)
        #now we check if the new stone captures anything, if so it's not suicide
        for neighbour in potentialBoard.neighbours(coordinates):
            if potentialBoard.getGroup(neighbour).colour != 'None' and \
                potentialBoard.getGroup(neighbour) != colour:
                    if potentialBoard.getGroup(neighbour).isCaptured(potentialBoard):
                        return False
        #finally check to see if the stone will be captured itself
        return group.isCaptured(potentialBoard)
    
    '''
    Get group, takes a coordinate.  Looks through the groups list,
    if its in a group returns the group.  If it is not returns None for id
    and 0 for colour.
    '''
 
    def getGroup(self, coordinates):
        nullGroup = DotMap(colour = 'None')
        nullGroup.id = None
        
        for group in self.groups:
            if group.isInGroup(coordinates):
                return group
        return nullGroup

    '''
    isPlayable returns true if not offBoard, isSuicide is true, and isEmpty is true. 
    '''
                    
    def isPlayable(self, coordinates, colour):
        return not self.offBoard(coordinates) and \
                self.isEmpty(coordinates) and \
                not self.isSuicide(coordinates,colour)

    '''
    returns true if the player given cannot play any legal move
    '''
    
    def noPlayableMoves(self, colour):
        for x in range(self.size):
            for y in range(self.size):
                if self.isPlayable((x,y), colour):
                    return False
        return True
    
    '''
    Adds the group to the list
    '''
    
    def addToGroups(self, group):
        self.groups.append(group)
        
    '''
    Removes a group from the list
    '''
    
    def deleteGroup(self, group):
        self.groups.remove(group)

from copy import deepcopy
from dotmap import DotMap
from group import Group
