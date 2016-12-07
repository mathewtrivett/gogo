import pygame
from element import Element

class Player(Element):
    
    def __init__(self, screen, parent, align,
                 text, font, BASELINEGRID, fontSizeRelative,
                 bgColour,contrastColour,
                 widthDecimalPercent,heightDecimalPercent,
                 isActive):

        super(Player, self).__init__(screen, parent, align,
                                     text, font, BASELINEGRID, fontSizeRelative,
                                     bgColour,contrastColour,
                                     widthDecimalPercent,heightDecimalPercent)
        self.isActive = isActive

    def setActive(self,padding):
        points = ((self.textX-padding*2, self.textY-padding),
                  (self.textX+self.textSize[0]+padding*2, self.textY-padding),
                  (self.textX+self.textSize[0]+padding*2,self.textY+self.textSize[1]+padding),
                  (self.textX-padding*2,self.textY+self.textSize[1]+padding))
        
        if self.isActive == True:
            pygame.draw.aalines(self.screen,self.contrastColour,True,points)
            pygame.draw.lines(self.screen, self.contrastColour, True, points, 5)
