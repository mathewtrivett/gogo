class Match:
    
    def __init__(self, size=9):
        self.players = [Player('B',300),Player('W',300)]
        self.currentPlayer = 0
        self.board = Board(size)
        self.territories = Board(size)
        self.previousBoard = self.board.getMatrix()
        self.currentBoard = self.board.getMatrix()
        self.cursor = Cursor(self.board)
        self.attemptedPlace = False
        self.handler = EventHandler()
        self.UI = UIMatch(size, self.handler)
        self.newGame = False
    '''
    Evaulates one turn, the return value indictates if the match should end
    '''
    def playTurn(self):
        stonePlaced = False        
        self.players[self.currentPlayer].passed = False
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
                           self.players[0].prisoners,self.players[1].prisoners,
                           self.cursor.coordinates)
            if self.players[self.currentPlayer].passed == True:
                break
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
                           self.players[0].prisoners,self.players[1].prisoners,
                        self.cursor.coordinates)
        self.end = False
        lastTurnPassed = False
        while(not self.end):
            self.playTurn()
            if self.players[0].passed == True and\
                self.players[1].passed ==True:
                self.end = True
            if self.players[0].resigned == True or\
                self.players[1].resigned == True:
                self.UI.drawEnd("Game Over")
                self.end = True
        while self.newGame == False:
            self.lookForInput()
        self.UI.quit()
        newMatch = Match(self.board.size)
        newMatch.matchLoop()

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
        if self.players[self.currentPlayer].time > 0:
            self.players[self.currentPlayer].time -= self.handler.getTimePassed()
        if self.handler.hasQuit():
            self.UI.quit()
        if self.UI.winScreen.primary_button.wasPressed() and\
            self.end == True:
            self.newGame = True
            
        if self.currentPlayer == 0:
            if self.UI.blackPlayer.quitButton.wasPressed():
                self.players[0].resigned = True
            if self.UI.blackPlayer.passButton.wasPressed():
                self.players[0].passed = True
            if self.handler.keyWasPressed(pygame.K_SPACE):
                self.attemptedPlace = True
            if self.handler.keyWasPressed(pygame.K_a):
                self.cursor.moveBy((-1,0))
            if self.handler.keyWasPressed(pygame.K_d):
                self.cursor.moveBy((1,0))
            if self.handler.keyWasPressed(pygame.K_w):
                self.cursor.moveBy((0,-1))
            if self.handler.keyWasPressed(pygame.K_s):
                self.cursor.moveBy((0,1))
                
        if self.currentPlayer == 1:
            if self.UI.whitePlayer.quitButton.wasPressed():
                self.players[1].resigned = True
            if self.UI.whitePlayer.passButton.wasPressed():
                self.players[1].passed = True
            if self.handler.keyWasPressed(pygame.K_BACKSPACE):
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
