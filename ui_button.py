import pygame
from ui_element import UIElement

class UIButton(UIElement):
    def __init__(self,screen,parent,
                 text, font,BASELINEGRID,fontSizeRelative, 
                 bgColour,contrastColour,hoverColour,
                 widthDecimalPercent,heightDecimalPercent,
                 action,left,top):

        super(UIButton, self).__init__(screen, parent,
                                     text,font,BASELINEGRID,fontSizeRelative,
                                     bgColour,contrastColour,
                                     widthDecimalPercent,heightDecimalPercent,
                                     left,top)
        self.action = action
        self.hoverColour = hoverColour
        
    def onHover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.bgColour = self.hoverColour
            self.draw()
            print("Hovering")

    def onClick(self):
        event = pygame.event.poll()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                print(self.action)