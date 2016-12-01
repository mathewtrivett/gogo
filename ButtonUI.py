class ButtonUI:

    def __init__(self, parent, text, bgColour, border,
                 font, fontSize, textColour, size, position,
                 action):
        
        self.parent = parent
        self.text = text
        self.bgColour = bgColour
        self.border = border
        self.font = font
        self.fontSize = fontSize
        self.textColour = textColour
        self.width, self.height = size
        self.x, self.y = position
        self.states = {}
        self.action = action

    def draw(self):
        font = pygame.font.Font(self.font, self.fontSize)
        font.render(self.text, True, self.textColour)
        pass
        
import pygame
