class Match:
    
    def __init__(self, size=9):
        self.players = [Player('B',100),Player('W',100)]
        self.currentPlayer = 0
        self.board = Board(size)
        self.territories = Board(size)
        self.previousBoard = self.board.getMatrix()
        self.currentBoard = self.board.getMatrix()
    
    '''
    Evaulates one turn, the return value indictates if the match should end
    '''
    def playTurn(self):
        pygame.init()
        DECREMENTCLOCK = pygame.USEREVENT+1
        pygame.time.set_timer(DECREMENTCLOCK, 1000)
        stonePlaced = False
        if self.board.noPlayableMoves(self.players[self.currentPlayer].colour):
            print("No possible moves, passing...")
            return "passed"
        while(not stonePlaced):
            move = input(self.players[self.currentPlayer].colour + " to play:")
            for e in pygame.event.get():
                if e.type == DECREMENTCLOCK:
                    self.players[self.currentPlayer].time -= 1
            if move == "pass":
                self.currentPlayer = (self.currentPlayer+1)%len(self.players)
                return "passed"
            elif move == "quit":
                return "quit"
            else:
                coordinate = tuple(map(int,move.split(',')))
                stonePlaced = self.players[self.currentPlayer].placeStone(self.board,coordinate,self.previousBoard)
        print(self.players[self.currentPlayer].time)
        self.currentPlayer = (self.currentPlayer+1)%len(self.players)
        self.previousBoard = self.currentBoard
        self.currentBoard = self.board.getMatrix()
        print(self.board)
        return "placedStone"
    
    '''
    The main loop of the match
    '''
    def matchLoop(self):
        end = False
        lastTurnPassed = False
        while(not end):
            move = self.playTurn()
            if move == "passed":
                if lastTurnPassed == True:
                    end = True
                    self.updateTerritory()
                    winners = []
                    winningScore = 0
                    for player in self.players:
                        if self.findScore(player) > winningScore:
                            winners = [player]
                            winningScore = self.findScore(player)
                        elif self.findScore(player) == winningScore:
                            winners = winners + [player]
                lastTurnPassed = True
            elif move == "quit":
                winner = (self.currentPlayer+1)%len(self.players).colour
                end = True
            elif move == "placedStone":
                lastTurnPassed = False
        print("Territory:\n"+str(self.territories))
        print("Board:\n"+str(self.board))
        winnerstr  = ""
        for winner in winners:
            winnerstr = winnerstr + winner.colour + "  with "\
                + str(self.findScore(player)) + ", "
        print("winner is " + winnerstr)

    '''
    Gives the current score of a player
    '''
    
    def findScore(self, player):
        score = player.prisoners
        for group in self.territories.groups:
            if group.colour == player.colour:
                score = score + len(group.coordinates)
        return score
    
    def updateTerritory(self):
        for x in range(self.board.size):
            for y in range(self.board.size):
                if self.board.isEmpty((x,y)) and \
                    self.territories.isEmpty((x,y)):
                    newGroup = Group("u", {(x,y)})
                    self.territories.addToGroups(newGroup)
                    self.evaluateTerritory((x,y), newGroup)

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

from board import Board
from player import Player
from group import Group
import pygame
