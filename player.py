class Player:
    
    def __init__(self, colour, time):
        self.colour = colour
        self.prisoners = 0
        self.time = time
    
    '''
    placeStone, checks that a move is legal, places a stone onto the specified
    spot of the specified board. Then evaluates merges, captures and prisoners
    returning a boolean which indicates if the move could be made.
    '''
    
    def placeStone(self, board, coordinate):
        if board.isPlayable(coordinate, self.colour):
            #check for ko here, will likely need to be implement with board
            #Create the group
            newGroup = Group(self.colour, {coordinate})
            board.addToGroups(newGroup)
            #merge with friendly groups
            for neighbour in board.neighbours(coordinate):
                if board.getGroup(neighbour).colour == self.colour:
                    newGroup.mergeGroup(board.getGroup(neighbour),board)
            #evaluate captures
            for neighbour in board.neighbours(coordinate):
                if board.getGroup(neighbour).colour != 'None' and \
                    board.getGroup(neighbour).colour != self.colour:
                        if board.getGroup(neighbour).isCaptured(board):
                            self.prisoners = self.prisoners + len(board.getGroup(neighbour).coordinates)
                            board.deleteGroup(board.getGroup(neighbour))
            return True
        return False
    
    '''
    Simple returns a boolean indicating if the player is out of time.
    '''
    def hasTime(self):
        return self.time > 0

from board import Board
from group import Group
