import pygame
from ui_element import UIElement

class UIGameBoard(UIElement):
    def __init__(self, screen, parent,
                text, font, BASELINEGRID, fontSizeRelative,
                bgColour, contrastColour,
                widthDecimalPercent, heightDecimalPercent,
                boardSize, lineWidth,left,top):
        super(UIGameBoard,self).__init__(screen, parent,
                                    text, font, BASELINEGRID, fontSizeRelative,
                                    bgColour, contrastColour,
                                    widthDecimalPercent, heightDecimalPercent,left,top)
        
        # Backboard
        self.boardSize = boardSize + 1 ## Board plus 1 as a way to build the iterator for lines
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
        return self.coordinates[coordinates[1]][coordinates[0]]
