import pygame
from ui_element import UIElement

class UIButton(UIElement):
    def __init__(self,screen,parent,
                 text, font,BASELINEGRID,fontSizeRelative, 
                 bgColour,contrastColour,hoverColour,
                 widthDecimalPercent,heightDecimalPercent,left,top, eventHandler):

        super(UIButton, self).__init__(screen, parent,
                                     text,font,BASELINEGRID,fontSizeRelative,
                                     bgColour,contrastColour,
                                     widthDecimalPercent,heightDecimalPercent,
                                     left,top)
        self.hoverColour = hoverColour
        self.eventHandler = eventHandler
        
    def draw(self):
        nonHoverColour = self.bgColour
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.bgColour = self.hoverColour
        super(UIButton, self).draw()
        self.bgColour = nonHoverColour

    def wasPressed(self):
        if self.eventHandler.leftClicked():
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        else :
            return False
