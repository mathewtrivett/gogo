import pygame

class ButtonUI():
    
    def __init__(self, parent, text, bgColour, font,
                 fontSize, textColour, position,
                 action):
        self.parent = parent
        self.text = text
        self.bgColour = bgColour
        self.font = font
        self.fontSize = fontSize
        self.textColour = textColour
        self.position = position
        self.action = action

    def draw(self):
        if pygame.font.get_init():
            font = pygame.font.Font(self.font, self.fontSize)
            buttonText = font.render(self.text, True, self.textColour, self.bgColour)
            self.parent.blit(buttonText,self.position)
        else:
            pygame.font.init()

    def onHover(self):
        pass

    def onClick(self):
        pass
