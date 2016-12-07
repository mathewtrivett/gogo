import pygame
from element import Element

class Timer(Element):

    def __init__(self,screen, parent, align,
                 text, font, BASELINEGRID, fontSizeRelative,
                 bgColour,contrastColour,
                 widthDecimalPercent,heightDecimalPercent):

        super(Timer,self).__init__(screen, parent, align,
                                 text, font, BASELINEGRID, fontSizeRelative,
                                 bgColour,contrastColour,
                                 widthDecimalPercent,heightDecimalPercent)
    def update(self):
        pass
