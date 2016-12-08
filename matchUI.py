import pygame
import pygame.gfxdraw
from stone import Stone
from button import Button
from gameboard import GameBoard
from element import Element
from player_ui import Player
from timer import Timer
from gameboard import GameBoard

class MatchUI():
    
    def __init__(self):
        self.WIDTH = 1024
        self.HEIGHT = 768
        self.FRAMERATE = 60
        self.BASELINE_GRID = self.WIDTH / 64

        ## Colours and Textures
        self.BOARDCOLOUR = pygame.color.THECOLORS['chocolate4']
        self.LINECOLOUR = pygame.color.THECOLORS['black']
        self.WHITESTONE = pygame.color.THECOLORS['antiquewhite1']
        self.BLACKSTONE = pygame.color.THECOLORS['grey10']
        self.PASS_BUTTON_COLOUR = pygame.color.THECOLORS['aquamarine3']
        self.QUIT_BUTTON_COLOUR = pygame.color.Color(233, 80, 80, 255)
        self.BUTTON_FONT_COLOUR = pygame.color.THECOLORS['black']


        # Fonts
        self.FONT = "./font/SourceSansPro-Regular.ttf"
        self.FONTSIZE = 2.2
        self.TIMER_FONTSIZE = 4.2
        self.BUTTON_FONTSIZE = 1.6

        ## SETUP Pygame Environment
        pygame.init()
        self.screen = pygame.display.set_mode([self.WIDTH,self.HEIGHT])
        pygame.display.set_caption("GoGo")
        
        
        ## Black's UI Elements
        self.black = Player(self.screen,self.screen,'topleft',0,0,
                'Black',self.FONT,self.BASELINE_GRID,self.FONTSIZE,
                self.BLACKSTONE,self.WHITESTONE,
                0.2,1,True,self.TIMER_FONTSIZE,self.BUTTON_FONTSIZE,
                    self.PASS_BUTTON_COLOUR, self.QUIT_BUTTON_COLOUR,
                    self.BUTTON_FONT_COLOUR)
        
        self.white = Player(self.screen,self.screen,'topright',0,0,
                'White',self.FONT,self.BASELINE_GRID,self.FONTSIZE,
                self.WHITESTONE,self.BLACKSTONE,
                0.2,1,False,self.TIMER_FONTSIZE,self.BUTTON_FONTSIZE,
                self.PASS_BUTTON_COLOUR, self.QUIT_BUTTON_COLOUR,
                self.BUTTON_FONT_COLOUR)

        self.board = GameBoard(self.screen,self.screen,'',0.2,0.06, 
                                "",self.FONT,self.BASELINE_GRID,self.FONTSIZE,
                                self.BOARDCOLOUR, self.BLACKSTONE, ## has whitestone for now
                                0.6,(self.WIDTH/self.HEIGHT)*0.6,9,1)
        
    def update(self):
        self.screen.fill(self.BOARDCOLOUR)
        self.board.update()
        self.black.update()
        self.white.update()
        
        while True:
            
            pygame.display.flip()
            event = pygame.event.poll()
            pygame.display.update()
    
            if event.type == pygame.QUIT :
                break   
        pygame.quit()