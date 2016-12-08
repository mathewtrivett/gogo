import pygame
from ui_element import UIElement

class UIButton(UIElement):
    def __init__(self,screen,parent,align,
                 text, font,BASELINEGRID,fontSizeRelative, 
                 bgColour,contrastColour,
                 widthDecimalPercent,heightDecimalPercent,
                 action):

        super(UIButton, self).__init__(screen, parent, align,
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

