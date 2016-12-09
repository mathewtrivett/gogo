from ui_match import UIMatch
from eventHandler import EventHandler
from ui_message import UIMessage
import pygame

class UIMainMenu(UIMatch):
    
    def __init__(self):
        
        self.eventHandler = EventHandler()
        
        super(UIMainMenu, self).__init__(9,self.eventHandler)
        
        #We tell the button to draw to a dummy screen so it does not appear
        self.winScreen.primary_button.screen = pygame.Surface((0,0))
        self.nineByNine = UIMessage(self.screen, self.screen,
                            "9x9",
                            self.FONT,self.BASELINE_GRID,self.MESSAGE_FONTSIZE,
                            pygame.color.Color(0,0,0,60),self.WHITESTONE,0.3,0.25,
                            self.BUTTON_FONTSIZE, self.BUTTON_FONT_COLOUR,
                            self.PASS_BUTTON_COLOUR,self.PASS_BUTTON_HOVER_COLOUR,
                            "Select",None, 0.35,0.05, self.eventHandler)
        self.thirteenByThirteen = UIMessage(self.screen, self.screen,
                            "13x13",
                            self.FONT,self.BASELINE_GRID,self.MESSAGE_FONTSIZE,
                            pygame.color.Color(0,0,0,60),self.WHITESTONE,0.3,0.25,
                            self.BUTTON_FONTSIZE, self.BUTTON_FONT_COLOUR,
                            self.PASS_BUTTON_COLOUR,self.PASS_BUTTON_HOVER_COLOUR,
                            "Select",None, 0.35,0.35, self.eventHandler)
        self.nineteenByNineteen = UIMessage(self.screen, self.screen,
                            "19x19",
                            self.FONT,self.BASELINE_GRID,self.MESSAGE_FONTSIZE,
                            pygame.color.Color(0,0,0,60),self.WHITESTONE,0.3,0.25,
                            self.BUTTON_FONTSIZE, self.BUTTON_FONT_COLOUR,
                            self.PASS_BUTTON_COLOUR,self.PASS_BUTTON_HOVER_COLOUR,
                            "Select",None, 0.35,0.65, self.eventHandler)        
    def draw(self):
        self.update([[]],0,300,300,0,0,(0,0))
        self.nineByNine.update()
        self.thirteenByThirteen.update()
        self.nineteenByNineteen.update()
        pygame.display.update()

    def mainLoop(self):
        self.draw()
        self.exit = False
        while self.exit == False:
            self.lookForInput()

    def lookForInput(self):
        self.eventHandler.update()
        if self.eventHandler.hasQuit():
            self.exit = True
            self.quit()
        if self.nineByNine.primary_button.wasPressed():
            self.quit()
            self.match = Match(9)
            self.match.matchLoop()
            self.exit = True
        elif self.thirteenByThirteen.primary_button.wasPressed():
            self.quit()
            self.match = Match(13)
            self.match.matchLoop()
            self.exit = True
        elif self.nineteenByNineteen.primary_button.wasPressed():
            self.quit()
            self.match = Match(19)
            self.match.matchLoop()
            self.exit = True


from match import Match
