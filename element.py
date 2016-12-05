import pygame

class Element():
    def __init__(self, screen, parent,
                 text, bgColour,contrastColour,
                 children, left, top, width, height):
        self.screen = screen
        self.parent = parent
        self.parentSize = self.parent.get_rect()
        self.bgColour = bgColour
        self.contrastColour = contrastColour
        self.children = [children]
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def draw(self):
        self.rect = pygame.draw.rect(
                    self.screen,
                    self.bgColour,
                    (self.left,self.top,
                    self.parentSize.width*self.width, self.parentSize.height*self.height))

    def alignTopLeft(self):
        self.rect.topleft = self.parentSize.topleft
        self.move(self.
        self.draw()

    def alignTopRight(self):
        self.rect.topright = self.parentSize.topright
        self.draw()
