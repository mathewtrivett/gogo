import pygame

class BoardUI():
    def __init__(self, grid, width, lineWidth, lineColour, boardColour,parent):
        self.grid = grid
        self.parent = parent
        self.parentWidth = self.parent.get_width()
        self.width = width
        self.divisor = grid + 1
        self.boardColour = boardColour

        # Backboard
        self.image = pygame.Surface((self.parentWidth * self.width, self.parentWidth * self.width))
        self.image.fill(self.boardColour)
        self.parent.blit(self.image, (self.parentWidth * 0.2, self.parentWidth * 0.05))
##        self.bg = pygame.draw.rect(self.parent, self.boardColour,
##                                   (self.parentWidth * 0.2, self.parentWidth * 0.05,
##                                    self.parentWidth * self.width, self.parentWidth * self.width))

        self.rect = self.image.get_rect()
        
        self.lineWidth = lineWidth # Sets the grid's line width
        self.lineColour = lineColour

        ## Dimensions
        self.interval = self.image.get_width() / self.divisor # Divides the background by the divisor
        self.origin = (self.rect.y + self.interval, self.rect.x + self.interval)
        self.farCorner = tuple(map(lambda x,y: x+self.interval*y, self.origin, (self.grid,self.grid)))
        self.coordinates = [[(x,y) for x in range(int(self.origin[0]), int(self.farCorner[0]), int(self.interval))] for y in range(int(self.origin[1]), int(self.farCorner[1]), int(self.interval))]

    def draw(self):       
        for position in range(self.divisor):
                if position == 0:
                    continue

                # Horizontal Grid
                pygame.draw.line(self.parent,
                            self.lineColour,
                             (self.rect.x + self.interval, self.rect.y + self.interval * position),
                             (self.rect.x + self.image.get_width() - self.interval, self.rect.y + self.interval * position),
                             self.lineWidth)
                
                # Vertical Grid
                pygame.draw.line(self.parent,
                                self.lineColour,
                                 (self.rect.x + self.interval * position, self.rect.y + self.interval),
                                 (self.rect.x + self.interval * position, self.image.get_height() + self.rect.y - self.interval),
                                 self.lineWidth)

    def returnCoords(self, pixelCoords):
        return self.coordinates[pixelCoords[0]][pixelCoords[1]]
