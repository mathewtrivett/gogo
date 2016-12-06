import pygame

class Element():
    def __init__(self, screen, parent, align,
                 text, bgColour,contrastColour,
                 children, left, top, widthDecimalPercent, heightDecimalPercent):
        self.screen = screen
        self.parent = parent
        self.parentSize = self.parent.get_rect()
        self.align = align
        self.bgColour = bgColour
        self.contrastColour = contrastColour
        self.children = [children]
        self.widthDecimalPercent = widthDecimalPercent
        self.heightDecimalPercent = heightDecimalPercent

        self.width = self.parentSize.width * self.widthDecimalPercent
        self.height = self.parentSize.height * self.heightDecimalPercent

        if self.align == 'topleft':
            self.x, self.y = self.parentSize.topleft
        if self.align == 'topright':
            self.x, self.y = (self.parentSize.topright[0] - self.width,self.parentSize.topright[1])

    def draw(self):
        self.rect = pygame.draw.rect(
                    self.screen,
                    self.bgColour,
                    (self.x,self.y,
                    self.width,self.height))

