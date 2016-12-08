import pygame

class UIGameBoard():

    def __init__(self, grid, width, lineColour,lineWidth,boardColour,parent):
        self.grid = grid # Board.size
        self.width = width # Width of the board as a decimal percentage of its parent.
        self.divisor = grid + 1
        self.boardColour = boardColour # The colour of the backboard
        self.parent = parent # The Board's parent

        # Backboard
        self.image = pygame.Surface((self.parent.get_width() * self.width, self.parent.get_width() * self.width))
        self.image.fill(self.boardColour)
        self.rect = self.image.get_rect()
        self.interval = int(self.rect.width / self.divisor) # Board's background size by the divisor
        self.topX = self.parent.get_width() * 0.2
        self.topY = self.parent.get_width() * 0.05
        self.gridTopX = int(self.topX + self.interval)
        self.gridTopY = int(self.topY + self.interval)
                
        ## Coordinates
        self.coordinates = [[(x,y) for x in range(self.gridTopX, int(self.topX+self.rect.width-self.interval), int(self.interval))] for y in range(self.gridTopY, int(self.topY+self.rect.height-self.interval), int(self.interval))]

        # Grid
        self.lineColour = lineColour
        self.lineWidth = lineWidth
         
        for position in range(self.divisor):
            if position == 0:
                continue

            # Horizontal Grid
            pygame.draw.line(self.image,
                        self.lineColour,
                         (int(self.rect.x + self.interval), int(self.rect.y + self.interval * position)),
                         (int(self.rect.x + self.image.get_width() - self.interval), int(self.rect.y + self.interval * position)),
                         self.lineWidth)
            
            # Vertical Grid
            pygame.draw.line(self.image,
                            self.lineColour,
                             (int(self.rect.x + self.interval * position), int(self.rect.y + self.interval)),
                             (int(self.rect.x + self.interval * position), int(self.image.get_height() + self.rect.y - self.interval)),
                             self.lineWidth)
        self.parent.blit(self.image, (self.topX, self.topY))

    def getPixelPos(self,coordinates):
        return self.coordinates[coordinates[1]][coordinates[0]]
