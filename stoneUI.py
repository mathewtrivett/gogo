import pygame
import pygame.gfxdraw

class StoneUI():
    
    def __init__(self, BoardUI, colour, coordinates, screen):
        self.screen = screen
        self.board = BoardUI
        self.diameter = BoardUI.interval - 3
        self.colour = colour
        self.coordinates = coordinates
        self.position = tuple(map(lambda x,y: x+self.board.interval*y, self.board.origin, coordinates))

    def show(self):
        pygame.gfxdraw.aacircle(self.screen,
                                int(self.position[1]),
                                int(self.position[0]),
                                int(self.diameter/2),
                                self.colour)
        
        pygame.gfxdraw.filled_circle(self.screen,
                                int(self.position[1]),
                                int(self.position[0]),
                                int(self.diameter/2),
                                self.colour)

    def move(self, mx, my):
        # self.coords = (self.coords[0]+mx,self.coords[1]+my)
        pass

    def place(self):
        pass

