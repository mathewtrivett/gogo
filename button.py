import pygame
from element import Element

class Button(Element):
    def __init__(self,screen,parent,align,
                 text, font,BASELINEGRID,fontSizeRelative, 
                 bgColour,contrastColour,
                 widthDecimalPercent,heightDecimalPercent,
                 action):

        super(Button, self).__init__(screen, parent, align,
                                     text,font,BASELINEGRID,fontSizeRelative,
                                     bgColour,contrastColour,
                                     widthDecimalPercent,heightDecimalPercent
                                     )
        self.action = action
        
    def onHover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            print("Hovering")

    def onClick(self):
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                print(self.action)

