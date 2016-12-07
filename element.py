import pygame

class Element():
    def __init__(self, screen, parent, align,
                 text, font, fontSize, textColour,
                 bgColour,contrastColour,
                 left, top, widthDecimalPercent,
                 heightDecimalPercent):
        self.screen = screen
        self.parent = parent
        if type(self.parent) == pygame.Surface:
            self.parentSize = self.parent.get_rect()
        else:
            self.parentSize = self.parent.rect
        self.align = align
        self.text = text
        self.font = font
        self.fontSize = fontSize
        self.textColour = textColour
        self.bgColour = bgColour
        self.contrastColour = contrastColour
        self.widthDecimalPercent = widthDecimalPercent
        self.heightDecimalPercent = heightDecimalPercent
        self.width = self.parentSize.width * self.widthDecimalPercent
        self.height = self.parentSize.height * self.heightDecimalPercent

        if self.align == 'topleft':
            self.x, self.y = self.parentSize.topleft
        if self.align == 'topright':
            self.x, self.y = (self.parentSize.topright[0] - self.width,self.parentSize.topright[1])
        if self.align == 'bottomleft':
            self.x, self.y = self.parentSize.bottomleft
        if self.align == 'bottomright':
            self.x, self.y = (self.parentSize.bottomright[0] - self.width,self.parentSize.bottomright[1])

    def draw(self):
        self.rect = pygame.draw.rect(
                    self.screen,
                    self.bgColour,
                    (self.x,self.y,
                    self.width,self.height))
