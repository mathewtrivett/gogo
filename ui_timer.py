import pygame
from ui_element import UIElement

class UITimer(UIElement):

    def __init__(self,screen, parent, align,
                 text, font, BASELINEGRID, fontSizeRelative,
                 bgColour,contrastColour,
                 widthDecimalPercent,heightDecimalPercent):

        super(UITimer,self).__init__(screen, parent, align,
                                 text, font, BASELINEGRID, fontSizeRelative,
                                 bgColour,contrastColour,
                                 widthDecimalPercent,heightDecimalPercent)
        
    def update(self,ticks):
        self.text = ticks
