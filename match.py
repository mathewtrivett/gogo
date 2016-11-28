class Match:
    
    def __init__(self, size=9):
        self.players = [Player('B',100),Player('W',100)]
        self.currentPlayer = 0
        self.board = Board(size)
        self.previousBoard = self.board.getMatrix()
        self.currentBoard = self.board.getMatrix()
    
    '''
    Evaulates one turn, the return value indictates if the match should end
    '''
    def playTurn(self):
        stonePlaced = False
        while(not stonePlaced):
            move = input(self.players[self.currentPlayer].colour + " to play:")
            if move == "pass":
                self.currentPlayer = (self.currentPlayer+1)%len(self.players)
                return "passed"
            elif move == "quit":
                return "quit"
            else:
                coordinate = tuple(map(int,move.split(',')))
                stonePlaced = self.players[self.currentPlayer].placeStone(self.board,coordinate,self.previousBoard)
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
                lastTurnPassed = True
            elif move == "quit":
                end = True
            elif move == "placedStone":
                lastTurnPassed = False

from board import Board
from player import Player
