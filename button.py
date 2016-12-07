import pygame
from element import Element

class Button(Element):
    def __init__(self,screen, parent,align,
                 text, font, fontSize, textColour,
                 bgColour,contrastColour,
                 left, top, widthDecimalPercent,
                 heightDecimalPercent,action):

        super(Button, self).__init__(screen, parent, align,
                                     text, font, fontSize, textColour,
                                     bgColour,contrastColour,
                                     left, top, widthDecimalPercent,
                                     heightDecimalPercent)
        self.action = action
        
    def onHover(self):
        pass

    def onClick(self):
        print(self.action)


## Button Text
# screen.blit(pass_Button,(black_pass.x + black_pass.width/2-pass_size[0]/2,blackPlayer.height+black_pass.height/2-pass_size[1]/2)) # screen
#screen.blit(pass_Button,(white_pass.x+white_pass.width/2-pass_size[0]/2,whitePlayer.height + white_pass.height/2-pass_size[1]/2))
#screen.blit(quit_Button,(black_quit.x + black_quit.width/2-quit_size[0]/2,blackPlayer.height+black_quit.height/2-quit_size[1]/2))
#screen.blit(quit_Button,(white_quit.x + white_quit.width/2-quit_size[0]/2,whitePlayer.height+white_quit.height/2-quit_size[1]/2))
