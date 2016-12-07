import pygame
from element import Element

class Button(Element):
    def __init__(self,screen,parent,align,
                 text, font,BASELINEGRID,fontSizeRelative, 
                 textColour,bgColour,contrastColour,
                 left,top,widthDecimalPercent,heightDecimalPercent,
                 action):

        super(Button, self).__init__(screen, parent, align,
                                     text, font, BASELINEGRID,fontSizeRelative,
                                     textColour,bgColour,contrastColour,
                                     left, top, widthDecimalPercent,heightDecimalPercent
                                     )
        self.action = action
        
    def onHover(self):
        pass

    def onClick(self):
        print(self.action)

