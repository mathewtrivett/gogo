import pygame
import pygame.gfxdraw

class Stone(pygame.sprite.Sprite):
    def __init__(self, boardUI, colour, screen):
        pygame.sprite.Sprite.__init__(self)
        self.board = boardUI
        self.screen = screen
        self.colour = colour
        self.radius = int(self.board.interval/2 - 3)
        self.coordinates = (0,0)
        self.isPlaced = False
        self.isPlayable = True
        self.image = pygame.Surface([self.board.interval,self.board.interval])
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        pygame.gfxdraw.aacircle(self.image,
                                self.rect.center[0],
                                self.rect.center[1],
                                self.radius,
                                self.colour)
        pygame.gfxdraw.filled_circle(self.image,
                                self.rect.center[0],
                                self.rect.center[1],
                                self.radius,
                                self.colour)
        self.rect.center = self.board.getPixelPos(self.coordinates)

    def update(self):
        print(self.coordinates,self.rect.center)
        self.step = 0
        if not self.isPlaced:
            keypress = pygame.key.get_pressed()
            if keypress[pygame.K_SPACE]:
                self.isPlaced = True
            if keypress[pygame.K_RIGHT]:
                self.step = 1
                if self.coordinates[0]+self.step > self.board.grid-1:
                    self.coordinates = (0, self.coordinates[1])
                else:
                    self.coordinates = (self.coordinates[0]+self.step,self.coordinates[1])
            if keypress[pygame.K_LEFT]:
                self.step = -1
                if self.coordinates[0]+self.step < 0:
                    self.coordinates = (self.board.grid -1, self.coordinates[1])
                else:
                    self.coordinates = (self.coordinates[0]+self.step,self.coordinates[1])
            if keypress[pygame.K_DOWN]:
                self.step = 1
                if self.coordinates[1]+self.step > self.board.grid -1:
                    self.coordinates = (self.coordinates[0], 0)
                else:
                    self.coordinates = (self.coordinates[0],self.coordinates[1]+self.step)
            if keypress[pygame.K_UP]:
                self.step = -1
                if self.coordinates[1]+self.step < 0:
                    self.coordinates = (self.coordinates[0], self.board.grid -1)
                else:
                    self.coordinates = (self.coordinates[0],self.coordinates[1]+self.step)
        self.rect.center = self.board.getPixelPos(self.coordinates)
