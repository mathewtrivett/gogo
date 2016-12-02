import pygame

class GameBoard():

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

        ## Coordinates
        self.interval = self.rect.width / self.divisor # Board's background size by the divisor
        self.coordinates = [[(x,y) for x in range(int(self.interval), self.rect.width-int(self.interval), int(self.interval))] for y in range(int(self.interval), self.rect.height-int(self.interval), int(self.interval))]

        # Grid
        self.lineColour = lineColour
        self.lineWidth = lineWidth
         
        for position in range(self.divisor):
            if position == 0:
                continue

            # Horizontal Grid
            pygame.draw.line(self.image,
                        self.lineColour,
                         (self.rect.x + self.interval, self.rect.y + self.interval * position),
                         (self.rect.x + self.image.get_width() - self.interval, self.rect.y + self.interval * position),
                         self.lineWidth)
            
            # Vertical Grid
            pygame.draw.line(self.image,
                            self.lineColour,
                             (self.rect.x + self.interval * position, self.rect.y + self.interval),
                             (self.rect.x + self.interval * position, self.image.get_height() + self.rect.y - self.interval),
                             self.lineWidth)
        self.parent.blit(self.image, (self.parent.get_width() * 0.2, self.parent.get_width() * 0.05))


    def getPixelPos(self,coordinates):
        return self.coordinates[coordinates[0]][coordinates[1]]
