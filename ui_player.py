import pygame
from ui_element import UIElement
from ui_text import UIText
from ui_button import UIButton

class UIPlayer(UIElement):
    
    def __init__(self, screen, parent,
                 text, font, BASELINEGRID, fontSizeRelative,
                 bgColour,contrastColour,
                 widthDecimalPercent,heightDecimalPercent,
                 isActive,TIMER_FONTSIZE,BUTTON_FONTSIZE,
                    PASS_BUTTON_COLOUR, PASS_BUTTON_HOVER_COLOUR, QUIT_BUTTON_COLOUR, QUIT_BUTTON_HOVER_COLOUR,
                    BUTTON_FONT_COLOUR,left, top):

        super(UIPlayer, self).__init__(screen, parent,
                                     text, font, BASELINEGRID, fontSizeRelative,
                                     bgColour,contrastColour,
                                     widthDecimalPercent,heightDecimalPercent,left,top)
        
        self.isActive = isActive

        self.timer = UIText(screen,self,
              "3:00",font,BASELINEGRID,TIMER_FONTSIZE,
              bgColour,contrastColour,
              1,0.2,0,0)
        
        self.prisoners = UIText(screen,self,
                    "Prisoners = 5",font, BASELINEGRID,BUTTON_FONTSIZE,
                    bgColour, contrastColour,
                1,0.05,0,0.3)
        
        self.quitButton = UIButton(screen,self,
                    'Quit',font,BASELINEGRID,BUTTON_FONTSIZE,
                    QUIT_BUTTON_COLOUR,BUTTON_FONT_COLOUR,QUIT_BUTTON_HOVER_COLOUR,
                    0.5,0.06,"Quit",0.5,0)

        self.passButton = UIButton(screen,self,
                    'Pass',font,BASELINEGRID,BUTTON_FONTSIZE,
                    PASS_BUTTON_COLOUR,BUTTON_FONT_COLOUR,PASS_BUTTON_HOVER_COLOUR,
                    0.5,0.06,"Pass",0,0)

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
        self.prisoners.draw()
        self.prisoners.positionText(0.5,0)
