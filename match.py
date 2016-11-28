class Match:
    
    def __init__(self, size=9):
        self.players = [Player('B',100),Player('W',100)]
        self.currentPlayer = 0
        self.board = Board(size)
        self.previousBoard = self.board.getMatrix()
        self.currentBoard = self.board.getMatrix()
    
    '''
    Evaulates one turn
    '''
    def playTurn(self):
        stonePlaced = False
        while(not stonePlaced):
            coordinate = tuple(map(int,input(self.players[self.currentPlayer].colour + " to play:").split(',')))
            stonePlaced = self.players[self.currentPlayer].placeStone(self.board,coordinate,self.previousBoard)
        
        self.currentPlayer = (self.currentPlayer+1)%len(self.players)
        self.previousBoard = self.currentBoard
        self.currentBoard = self.board.getMatrix()
        print(self.board)
        
    '''
    The main loop of the match
    '''
    def matchLoop(self):
        while(True):
            self.playTurn()
    
from board import Board
from player import Player
