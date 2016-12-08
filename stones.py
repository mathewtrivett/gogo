import pygame
import pygame.gfxdraw
from element import Element
from stone import Stone

class Stones(Element):
    
    def __init__(self, stoneMatrix
                 ,screen, parent, align,
                text,font,BASELINEGRID,fontSizeRelative,
                bgColour,contrastColour,
                widthDecimalPercent,heightDecimalPercent, board):
        
        super(Stones, self).__init__(screen, parent, align,
                                     text,font,BASELINEGRID,fontSizeRelative,
                                     bgColour,contrastColour,
                                     widthDecimalPercent,heightDecimalPercent)
        self.screen = screen
        self.parent = parent
        self.board = board
        self.whiteColour = bgColour
        self.blackColour = contrastColour
        self.setStones(stoneMatrix)

        
    def setStones(self,stoneMatrix):
        self.whiteStones = []
        self.blackStones = []
        for (y,row) in enumerate(stoneMatrix):
            for (x,stone) in enumerate(row):
                if stone == "B":
                    self.blackStones.append((x,y))
                elif stone == "W":
                    self.whiteStones.append((x,y))
                    
    def update(self):
        for (x,y) in self.whiteStones:
            stone = Stone(self.board, self.whiteColour, self.screen)
            stone.coordinates = (x,y)
            stone.draw()
        for (x,y) in self.blackStones:
            stone = Stone(self.board, self.blackColour, self.screen)
            stone.coordinates = (x,y)
            stone.draw()
        
