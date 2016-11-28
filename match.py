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
        if self.board.noPlayableMoves(self.players[self.currentPlayer].colour):
            print("No possible moves, passing...")
            return "passed"
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
                    if self.findScore(0) > self.findScore(1):
                        winner = self.players[0].colour
                    else:
                        winner = self.players[1].colour
                lastTurnPassed = True
            elif move == "quit":
                winner = (self.currentPlayer+1)%len(self.players).colour
                end = True
            elif move == "placedStone":
                lastTurnPassed = False
        print("winner is " + winner)

    '''
    Gives the current score of a player
    '''
    
    def findScore(self, player):
        score = self.players[player].prisoners
        #for now terratory is ignored
        return score
from board import Board
from player import Player
