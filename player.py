class Player:
    
    def __init__(self, colour, time):
        self.colour = colour
        self.prisoners = 0
        self.time = time
        self.passed = False
        self.resigned = False
    
    '''
    placeStone, checks that a move is legal, places a stone onto the specified
    spot of the specified board. Then evaluates merges, captures and prisoners
    returning a boolean which indicates if the move could be made.
    '''
    
    def placeStone(self, currentBoard, coordinate, previousBoard = [[]]):
        if currentBoard.isPlayable(coordinate, self.colour):
            #everything is applied to newBoard first, for evaluating ko
            newBoard = deepcopy(currentBoard)
            newPrisoners = 0
            #Create the group
            newGroup = Group(self.colour, {coordinate})
            newBoard.addToGroups(newGroup)
            #merge with friendly groups
            for neighbour in newBoard.neighbours(coordinate):
                if newBoard.getGroup(neighbour).colour == self.colour:
                    newGroup.mergeGroup(newBoard.getGroup(neighbour),newBoard)
            #evaluate captures
            for neighbour in newBoard.neighbours(coordinate):
                if newBoard.getGroup(neighbour).colour != 'None' and \
                    newBoard.getGroup(neighbour).colour != self.colour:
                        if newBoard.getGroup(neighbour).isCaptured(newBoard):
                            captured_sound = UISound('./sounds/prisoners_captured/')
                            captured_sound.update()
                            newPrisoners = newPrisoners + len(newBoard.getGroup(neighbour).coordinates)
                            newBoard.deleteGroup(newBoard.getGroup(neighbour))
            #check for ko
            if newBoard.getMatrix() != previousBoard:
                place_stone_sound = UISound('./sounds/stone_placed/')
                place_stone_sound.update()
                currentBoard.setTo(newBoard)
                self.prisoners = self.prisoners + newPrisoners
                return True
        return False
    
    '''
    Simple returns a boolean indicating if the player is out of time.
    '''
    def hasTime(self):
        return self.time > 0

from board import Board
from copy import deepcopy
from group import Group
import pygame
from ui_sound import UISound