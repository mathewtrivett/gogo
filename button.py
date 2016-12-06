import pygame

class Button(Element):
    def __init__(self, screen, parent, text, bgColour, font,
                 fontSize, textColour,side,width,height,
                 action):
        self.screen = screen
        self.parent = parent
        self.text = text
        self.bgColour = bgColour
        self.font = font
        self.fontSize = fontSize
        self.textColour = textColour
        self.side = side
        self.width = width
        self.height = height
        self.action = action
        if self.side == 'left':
            self.rect = pygame.draw.rect(
                            self.screen,
                            self.bgColour
                            (self.parent.children[0].rect.bottomleft,(self.parent/2,self.screen * height))
        )
        elif self.side == 'right':
            self.rect = pygame.draw.rect(
                            self.screen,
                            self.bgColour
                            (self.parent.children[1].rect.topright,(self.parent/2,self.screen * height))
        )

    def draw(self):
        if pygame.font.get_init():
            font = pygame.font.Font(self.font, self.fontSize)
 #           self.textPosition = (self.,font.size(self.text)/2)
 #           buttonText = font.render(self.text, True, self.textColour)
 #           self.screen.blit(buttonText,self.textPosition)
        else:
            pygame.font.init()
            draw(self)

    def onHover(self):
        pass

    def onClick(self):
        print(self.action)

## Buttons
# (0,whitePlayer.height,whitePlayer.width/2,HEIGHT*0.05)) # self.screen, self.button.colour(), (self.parent.width/2,self.screen.height * self.height)
white_pass = pygame.draw.rect(screen,PASS_BUTTON_COLOUR,(blackPlayer.x,blackPlayer.height,blackPlayer.width/2,HEIGHT*0.05)) # self.screen, self.button.colour, 

black_quit = pygame.draw.rect(screen,QUIT_BUTTON_COLOUR,(black_pass.width,blackPlayer.height,WIDTH*0.2/2,HEIGHT*0.05)) # self.screen, self.button.colour(), (self.parent.width/2,self.screen.height * self.height)
white_quit = pygame.draw.rect(screen,QUIT_BUTTON_COLOUR,(WIDTH-white_pass.width,whitePlayer.height,WIDTH,HEIGHT*0.05))

## Button Text
screen.blit(pass_Button,(black_pass.x + black_pass.width/2-pass_size[0]/2,blackPlayer.height+black_pass.height/2-pass_size[1]/2)) # screen
screen.blit(pass_Button,(white_pass.x+white_pass.width/2-pass_size[0]/2,whitePlayer.height + white_pass.height/2-pass_size[1]/2))
screen.blit(quit_Button,(black_quit.x + black_quit.width/2-quit_size[0]/2,blackPlayer.height+black_quit.height/2-quit_size[1]/2))
screen.blit(quit_Button,(white_quit.x + white_quit.width/2-quit_size[0]/2,whitePlayer.height+white_quit.height/2-quit_size[1]/2))
