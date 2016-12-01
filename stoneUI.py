import pygame
import pygame.gfxdraw

class StoneUI(pygame.sprite.Sprite):
    
    def __init__(self, boardUI, name, img, coordinates, screen):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.board = boardUI
        self.size = self.board.interval - 3
        self.image = pygame.transform.scale(pygame.image.load(img),(int(self.size),int(self.size)))
        self.screen = screen
        self.isPlaced = False
        self.isPlayable = True
        self.coordinates = coordinates
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = tuple(map(lambda x,y: int(x+self.board.interval*y), self.board.origin, coordinates))

        
    def draw(self):
        self.screen.blit(self.image,(self.rect.x,self.rect.y))
        
##        pygame.gfxdraw.aacircle(self.screen,
##                                int(self.position[1]),
##                                int(self.position[0]),
##                                int(self.diameter/2),
##                                self.colour)
##        
##        pygame.gfxdraw.filled_circle(self.screen,
##                                int(self.position[1]),
##                                int(self.position[0]),
##                                int(self.diameter/2),
##                                self.colour)
       
    def move(self, mx, my):
        pass


    def place(self):
        pass

