class Board:
    def __init__(self,size):
        self.size = size
        self.matrix = [['None' for x in range(self.size)] for y in range(self.size)]
        self.groups = []

    def __str__(self):
        state = ""
        for row in self.matrix:
            for col in row:
                state += col + " "
            state += "\n"
        return state

    def offBoard(self,coordinates):
        offBoard = False
        for (coordinate) in coordinates:
            if coordinate > self.size-1  or coordinate < 0:
                offBoard = True
        return offBoard

    ## Currently this is looking in the Matrix for empty spaces, we arn't
    ## Updating the matrix so will always return true

    def isEmpty(self, coordinates):
        return self.matrix[coordinates[0]][coordinates[1]] == 'None'

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
        group = Group(colour,{coordinates},isVirtual=True)
        for neighbour in self.neighbours(coordinates):
            if self.getGroup(neighbour).colour == group.colour:
                group.mergeGroup(self.getGroup(neighbour),self)
        return group.isCaptured(self)
    
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
        return self.isEmpty(coordinates) and not self.offBoard(coordinates) and not self.isSuicide(coordinates,colour)

    # addToGroups is called when 
    
    def addToGroups(self, group):
        self.groups.append(group)
        self.updateIds()

    def deleteGroup(self, group):
        self.groups.remove(group)
        self.updateIds()

    # updateIds enumerates over the board's groups and sets each group
    # id to be its index in the list
    
    def updateIds(self):
        for index, group in enumerate(self.groups):
            group.id = index

from group import Group
from dotmap import DotMap
