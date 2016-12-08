class Match:
    
    def __init__(self, size=9):
        self.players = [Player('B',10),Player('W',100)]
        self.currentPlayer = 0
        self.board = Board(size)
        self.territories = Board(size)
        self.previousBoard = self.board.getMatrix()
        self.currentBoard = self.board.getMatrix()
        self.UI = UIMatch(size)
        self.cursor = Cursor(self.board)
        self.attemptedPlace = False
        self.handler = EventHandler()
    '''
    Evaulates one turn, the return value indictates if the match should end
    '''
    def playTurn(self):
        stonePlaced = False
        if self.board.noPlayableMoves(self.players[self.currentPlayer].colour):
            print("No possible moves, passing...")
            self.players[self.currentPlayer].passed = True
        while(not stonePlaced):
            if self.players[self.currentPlayer].time <= 0:
                self.players[self.currentPlayer].passed = True
            self.attemptedPlace = False
            self.lookForInput()
            self.UI.update(self.currentBoard, self.currentPlayer,
                           self.players[0].time,self.players[1].time,
                           self.cursor.coordinates)
            print("a")
            if self.players[self.currentPlayer].passed == True:
                break
            print("b")
            if self.players[self.currentPlayer].resigned == True:
                break
            if self.attemptedPlace == True:
                if self.players[self.currentPlayer].placeStone(
                    self.board,self.cursor.coordinates,
                    self.previousBoard) == True:
                    break
        self.currentPlayer = (self.currentPlayer+1)%len(self.players)
        self.previousBoard = self.currentBoard
        self.currentBoard = self.board.getMatrix()
    
    '''
    The main loop of the match
    '''
    def matchLoop(self):
        self.UI.update(self.currentBoard, self.currentPlayer,
                        self.players[0].time,self.players[1].time,
                        self.cursor.coordinates)
        end = False
        lastTurnPassed = False
        while(not end):
            self.playTurn()
            if self.players.[currentPlayer].passed == True and\
                self.players.[currentPlayer+1%len(self.players)].passed ==True:
                #end game
            if self.players.[currentPlayer].resigned == True:
                #also end game
        self.UI.quit()

    '''
    Gives the current score of a player
    '''
    
    def findScore(self, player):
        score = player.prisoners
        for group in self.territories.groups:
            if group.colour == player.colour:
                score = score + len(group.coordinates)
        return score
    
    '''
    updates self.territories to represent the current state of board
    '''
    
    def updateTerritory(self):
        for x in range(self.board.size):
            for y in range(self.board.size):
                if self.board.isEmpty((x,y)) and \
                    self.territories.isEmpty((x,y)):
                    newGroup = Group("u", {(x,y)})
                    self.territories.addToGroups(newGroup)
                    self.evaluateTerritory((x,y), newGroup)

    '''
    called recursively by updateTerritory() to evaluate a territory group
    '''
    
    def evaluateTerritory(self, position, group):
        for neighbour in self.territories.neighbours(position):
            if self.territories.isEmpty(neighbour):
                if self.board.isEmpty(neighbour):
                    newGroup = Group(group.colour, {neighbour})
                    self.territories.addToGroups(newGroup)
                    group.mergeGroup(newGroup, self.territories)
                    self.evaluateTerritory(neighbour, group)
                elif self.board.getGroup(neighbour).colour != group.colour:
                    if group.colour == "u":
                        group.colour = self.board.getGroup(neighbour).colour
                    else:
                        group.colour = "n"

    '''
    Looks for any of the allowed inputs to any resolves the relvent action
    '''
    def lookForInput(self):
        self.handler.update()
        self.players[self.currentPlayer].time -= self.handler.getTimePassed()
        if self.handler.hasQuit():
            self.UI.quit()
        if self.handler.keyWasPressed(pygame.K_SPACE):
            self.attemptedPlace = True
        if self.handler.keyWasPressed(pygame.K_LEFT):
            self.cursor.moveBy((-1,0))
        if self.handler.keyWasPressed(pygame.K_RIGHT):
            self.cursor.moveBy((1,0))
        if self.handler.keyWasPressed(pygame.K_UP):
            self.cursor.moveBy((0,-1))
        if self.handler.keyWasPressed(pygame.K_DOWN):
            self.cursor.moveBy((0,1))
            
from cursor import Cursor
from eventHandler import EventHandler
from board import Board
from player import Player
from group import Group
import pygame
from ui_match import UIMatch
