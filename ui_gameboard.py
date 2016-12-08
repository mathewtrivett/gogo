import pygame
from element import Element

class UIGameBoard(Element):
    def __init__(self, screen, parent, align,left,top,
                text, font, BASELINEGRID, fontSizeRelative,
                bgColour, contrastColour,
                widthDecimalPercent, heightDecimalPercent,
                boardSize, lineWidth):
        super(GameBoard,self).__init__(screen, parent, align,left,top,
                                    text, font, BASELINEGRID, fontSizeRelative,
                                    bgColour, contrastColour,
                                    widthDecimalPercent, heightDecimalPercent)
        
        # Backboard
        self.boardSize = boardSize ## Board plus 1 as a way to build the iterator for lines
        self.x = (self.parentSize.x + self.parentSize.width) * left
        self.y = (self.parentSize.y + self.parentSize.height) * top
        self.interval = self.width / self.boardSize # Board's background size by the divisor
        
        # Grid
        self.lineWidth = lineWidth
        
        ## Coordinates
        self.coordinates = [[(x,y) for x in range(int(self.x+self.interval), int(self.x+self.width-self.interval), int(self.interval))]
                            for y in range(int(self.y+self.interval), int(self.y+self.rect.height-self.interval), int(self.interval))]
 
    def update(self):
        self.draw()
        for position in range(len(self.coordinates)):

            # Horizontal Lines
            pygame.draw.line(self.screen,
                             self.contrastColour,
                            (self.getPixelPos((0,position))),
                            (self.getPixelPos((len(self.coordinates)-1,position))),
                            self.lineWidth)

            # Vertical Lines
            pygame.draw.line(self.screen,
                            self.contrastColour,
                            (self.getPixelPos((position,0))),
                            (self.getPixelPos((position,len(self.coordinates)-1))),
                            self.lineWidth)

    def getPixelPos(self,coordinates):
        return self.coordinates[1],self.coordinates[0]