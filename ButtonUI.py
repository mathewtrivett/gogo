import pygame

class Button():
    
    def __init__(self, screen, parent, text, bgColour, font,
                 fontSize, textColour,x, y,width,height,
                 action):
        self.screen = screen
        self.parent = parent
        self.text = text
        self.bgColour = bgColour
        self.font = font
        self.fontSize = fontSize
        self.textColour = textColour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.action = action
        self.button = pygame.draw.rect(
                    )

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
