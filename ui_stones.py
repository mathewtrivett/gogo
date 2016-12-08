import pygame
import pygame.gfxdraw
from ui_element import UIElement
from ui_stone import UIStone

class UIStones(UIElement):
    
    def __init__(self, stoneMatrix
                 ,screen, parent, align,
                text,font,BASELINEGRID,fontSizeRelative,
                bgColour,contrastColour,
                widthDecimalPercent,heightDecimalPercent, board):
        
        super(UIStones, self).__init__(screen, parent, align,
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
            stone = UIStone(self.board, self.whiteColour, self.screen)
            stone.coordinates = (x,y)
            stone.draw()
        for (x,y) in self.blackStones:
            stone = UIStone(self.board, self.blackColour, self.screen)
            stone.coordinates = (x,y)
            stone.draw()
        
