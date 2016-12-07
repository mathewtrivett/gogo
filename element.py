import pygame

class Element():
    def __init__(self, screen, parent, align,
                 text, font, BASELINEGRID, fontSizeRelative,
                 textColour,bgColour,contrastColour,
                 left, top, widthDecimalPercent,heightDecimalPercent
                 ):
        self.screen = screen
        self.parent = parent
        if type(self.parent) == pygame.Surface:
            self.parentSize = self.parent.get_rect()
        else:
            self.parentSize = self.parent.rect
        self.align = align
        self.text = text
        self.font = font
        self.BASELINE_GRID = BASELINEGRID
        self.fontSize = fontSizeRelative
        self.textColour = textColour
        self.bgColour = bgColour
        self.contrastColour = contrastColour
        self.widthDecimalPercent = widthDecimalPercent
        self.heightDecimalPercent = heightDecimalPercent
        self.width = int(self.parentSize.width * self.widthDecimalPercent)
        self.height = int(self.parentSize.height * self.heightDecimalPercent)

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

    def positionText(self, x, y):
        font = pygame.font.Font(self.font,
                                int(self.BASELINE_GRID*self.fontSize))
        self.textSize = font.size(self.text)
        text = font.render(self.text,True,self.textColour)
        self.screen.blit(text,
                         (self.x+(self.width)*x-self.textSize[0]*x,
                          self.y+(self.height)*y-self.textSize[1]*y))
