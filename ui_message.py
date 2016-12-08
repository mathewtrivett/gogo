import pygame
from ui_button import UIButton
from ui_element import UIElement

class UIMessage(UIElement):
    def __init__(self, screen, parent,
                 text, font, BASELINEGRID, fontSizeRelative,
                 bgColour,contrastColour,
                 widthDecimalPercent,heightDecimalPercent,
                 BUTTON_FONTSIZE, BUTTON_FONT_COLOUR,
                 PRIMARY_BUTTON_COLOUR, PRIMARY_BUTTON_HOVER_COLOUR,
                 PRIMARY_BUTTON_ACTION,PRIMARY_BUTTON_TEXT,
                 secondary_button,left, top):

        super(UIMessage, self).__init__(screen, parent,
                text, font, BASELINEGRID, fontSizeRelative,
                bgColour,contrastColour,
                widthDecimalPercent,heightDecimalPercent,left,top)

        self.primary_button = UIButton(screen, self,
                PRIMARY_BUTTON_TEXT, font, BASELINEGRID, BUTTON_FONTSIZE, 
                PRIMARY_BUTTON_COLOUR, BUTTON_FONT_COLOUR, PRIMARY_BUTTON_HOVER_COLOUR,
                0.2, 0.12,
                PRIMARY_BUTTON_ACTION, 0.4, 0.7)

        self.secondary_button = secondary_button

    def draw(self):
        surface = pygame.Surface((self.width, self.height))
        message = pygame.draw.rect(
                    surface,
                    self.bgColour,
                    (self.x,self.y,
                    self.width,self.height))
        surface.set_alpha(128)
        self.screen.blit(surface,(self.x,self.y))
 
    def update(self):
        self.draw()
        self.positionText(0.5,0.5)
        self.primary_button.draw()
        self.primary_button.positionText(0.5,0.5)
        self.primary_button.onHover()
        self.primary_button.onClick()