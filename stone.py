import pygame
import pygame.gfxdraw

class Stone():
    def __init__(self, board, colour, screen):
        self.board = board
        self.screen = screen
        self.colour = colour
        self.radius = int(self.board.interval/2 - 3)
        self.coordinates = (0,0)
        self.image = pygame.Surface((screen.get_width(),screen.get_width()))
        self.image.set_colorkey((0,0,0))

    def draw(self):
        center = self.board.getPixelPos(self.coordinates)
        
        self.rect = pygame.gfxdraw.aacircle(self.image,
                                center[0],
                                center[1],
                                self.radius,
                                self.colour)
        self.rect = pygame.gfxdraw.filled_circle(self.image,
                                center[0],
                                center[1],
                                self.radius,
                                self.colour)
        self.screen.blit(self.image,(0,0))
        
