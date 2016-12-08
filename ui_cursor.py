import pygame

class UICursor():
    
    def __init__(self, board, screen, colour):
        self.coordinates = (0,0)
        
        self.image = pygame.Surface((screen.get_width(),screen.get_width()))
        self.image.set_colorkey((0,0,0))
        self.board = board
        self.colour = colour
        self.screen = screen
        
    def draw(self):
        center = self.board.getPixelPos(self.coordinates)
        radius = self.board.interval/2
        
        self.rect = pygame.draw.line(self.image,self.colour,
                                     (center[0]-radius,center[1]),
                                     (center[0]+radius,center[1]),
                                     5)
        self.rect = pygame.draw.line(self.image,self.colour,
                                     (center[0],center[1]-radius),
                                     (center[0],center[1]+radius),
                                     5)
        self.screen.blit(self.image,(0,0))
    
