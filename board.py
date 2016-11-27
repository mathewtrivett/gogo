class Board:
    def __init__(self,size):
        self.size = size
        self.matrix = [['None' for x in range(self.size)] for y in range(self.size)]
        self.groups = []

    def offBoard(self,coordinates):
        offBoard = False
        for (coordinate) in coordinates:
            if coordinate > self.size-1  or coordinate < 0:
                offBoard = True
        return offBoard

    ## Currently this is looking in the Matrix for empty spaces, we arn't
    ## Updating the matrix so will always return true

    def isEmpty(self, coordinates):
        return self.matrix[coordinates[0]][coordinates[1]] == 0

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
        print(group.coordinates)
        print(self.neighbours((0,0)))
        for neighbour in self.neighbours(coordinates):
            if self.getGroup(neighbour).colour == group.colour:
                group.mergeGroup(self.getGroup(neighbour),self)
        print(group.coordinates)
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
    isPlayable returns true if, onboard is true, isEmpty and isNotSuicide. 
    '''
                    
    def isPlayable(self, coordinates, colour):
        return self.isEmpty(coordinates) and not self.isSuicide(coordinates,colour) and not self.offBoard(coordinates)
        
    def addGroup(self, group):
        self.groups = self.groups + [group]

    def deleteGroup(self, group):
        pass

from group import Group
from dotmap import DotMap
