import pygame
from ui_element import UIElement
from ui_timer import UITimer
from ui_button import UIButton

class UIPlayer(UIElement):
    
    def __init__(self, screen, parent, align,
                 text, font, BASELINEGRID, fontSizeRelative,
                 bgColour,contrastColour,
                 widthDecimalPercent,heightDecimalPercent,
                 isActive,TIMER_FONTSIZE,BUTTON_FONTSIZE,
                    PASS_BUTTON_COLOUR, QUIT_BUTTON_COLOUR,
                    BUTTON_FONT_COLOUR):

        super(UIPlayer, self).__init__(screen, parent, align,
                                     text, font, BASELINEGRID, fontSizeRelative,
                                     bgColour,contrastColour,
                                     widthDecimalPercent,heightDecimalPercent)
        self.isActive = isActive

        self.timer = UITimer(screen,self,'topleft',
              "3:00",font,BASELINEGRID,TIMER_FONTSIZE,
              bgColour,contrastColour,
              1,0.2)
        
        self.quitButton = UIButton(screen,self,'topright',
                    'Quit',font,BASELINEGRID,BUTTON_FONTSIZE,
                    QUIT_BUTTON_COLOUR,BUTTON_FONT_COLOUR,
                    0.5,0.06,"Quit")

        self.passButton = UIButton(screen,self,'topleft',
                    'Pass',font,BASELINEGRID,BUTTON_FONTSIZE,
                    PASS_BUTTON_COLOUR,BUTTON_FONT_COLOUR,
                    0.5,0.06,"Pass")

    def drawActivePlayerBorder(self,padding):
        points = ((self.textX-padding*2, self.textY-padding),
                  (self.textX+self.textSize[0]+padding*2, self.textY-padding),
                  (self.textX+self.textSize[0]+padding*2,self.textY+self.textSize[1]+padding),
                  (self.textX-padding*2,self.textY+self.textSize[1]+padding))
        
        if self.isActive == True:
            pygame.draw.aalines(self.screen,self.contrastColour,True,points)
            pygame.draw.lines(self.screen, self.contrastColour, True, points, 5)

    def update(self):
        self.draw()
        self.positionText(0.5,0.24)
        self.timer.draw()
        self.timer.positionText(0.5,1)
        self.drawActivePlayerBorder(int(self.BASELINE_GRID/3))
        self.quitButton.draw()
        self.quitButton.positionText(0.5,0.5)
        self.passButton.draw()
        self.passButton.positionText(0.5,0.5)
