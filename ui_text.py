import pygame
from ui_element import UIElement

class UIText(UIElement):

    def __init__(self,screen, parent,
                 text, font, BASELINEGRID, fontSizeRelative,
                 bgColour,contrastColour,
                 widthDecimalPercent,heightDecimalPercent,left,top):

        super(UIText,self).__init__(screen, parent,
                                 text, font, BASELINEGRID, fontSizeRelative,
                                 bgColour,contrastColour,
                                 widthDecimalPercent,heightDecimalPercent,left,top)
        
    def update(self,ticks):
        self.text = ticks
