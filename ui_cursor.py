import pygame

class UICursor():
    
    def __init__(self, board, screen, colour):
        self.coordinates = (0,0)
        
        self.board = board
        self.colour = colour
        self.screen = screen
        
    def draw(self):
        image = pygame.Surface((self.screen.get_width(),self.screen.get_width()))
        image.set_colorkey((0,0,0))
        center = self.board.getPixelPos(self.coordinates)
        radius = self.board.interval/2
        
        self.rect = pygame.draw.line(image,self.colour,
                                     (center[0]-radius,center[1]),
                                     (center[0]+radius,center[1]),
                                     5)
        self.rect = pygame.draw.line(image,self.colour,
                                     (center[0],center[1]-radius),
                                     (center[0],center[1]+radius),
                                     5)
        self.screen.blit(image,(0,0))
    
