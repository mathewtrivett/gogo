import pygame
import math

class Stone():
    def __init__(self, boardUI, name, img, coordinates):
        pygame.sprite.Sprite.__init__(self)
        
        self.board = boardUI
        self.name = name
        self.size = math.ceil(self.board.interval - 3)
        self.image = pygame.transform.scale(pygame.image.load(img),(self.size,self.size))
        self.coordinates = coordinates
        self.rect = self.image.get_rect()
        self.rect.center = self.board.getPixelPos(self.coordinates)
        self.isPlaced = False
        self.isPlayable = True

    def draw(self,surface):
        surface.blit(self.image,self.rect.center)
  
    def place(self):
        self.isPlaced = True
