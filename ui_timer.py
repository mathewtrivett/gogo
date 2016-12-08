import pygame
from ui_element import UIElement

class UITimer(UIElement):

    def __init__(self,screen, parent,
                 text, font, BASELINEGRID, fontSizeRelative,
                 bgColour,contrastColour,
                 widthDecimalPercent,heightDecimalPercent,left,top):

        super(UITimer,self).__init__(screen, parent,
                                 text, font, BASELINEGRID, fontSizeRelative,
                                 bgColour,contrastColour,
                                 widthDecimalPercent,heightDecimalPercent,left,top)
        
    def update(self,ticks):
        self.text = ticks
