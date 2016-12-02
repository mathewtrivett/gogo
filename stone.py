import pygame
import pygame.gfxdraw

class Stone():
    def __init__(self, boardUI, colour, coordinates,screen):
        self.board = boardUI
        self.screen = screen
        self.colour = colour
        self.radius = int(self.board.interval/2 - 3)
        self.coordinates = coordinates
        self.isPlaced = False
        self.isPlayable = True
        pygame.gfxdraw.aacircle(self.screen,
                                self.board.getPixelPos(self.coordinates)[0],
                                self.board.getPixelPos(self.coordinates)[1],
                                self.radius,
                                self.colour)
        pygame.gfxdraw.filled_circle(self.screen,
                                self.board.getPixelPos(self.coordinates)[0],
                                self.board.getPixelPos(self.coordinates)[1],
                                self.radius,
                                self.colour)

    def move(self):
        keypress = pygame.key.get_pressed()
        if keypress == pygame.key[K_RIGHT]:
            print("Right")

    def place(self):
        self.isPlaced = True
