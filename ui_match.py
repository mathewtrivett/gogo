import pygame
import pygame.gfxdraw
from ui_stone import UIStone
from ui_button import UIButton
from ui_gameboard import UIGameBoard
from ui_element import UIElement
from ui_player import UIPlayer
from ui_stones import UIStones
from ui_cursor import UICursor
from ui_message import UIMessage

class UIMatch():
    
    def __init__(self,boardSize, eventHandler):
        self.boardSize = boardSize
        self.eventHandler = eventHandler

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
        self.PASS_BUTTON_HOVER_COLOUR = pygame.color.Color(82, 185, 150, 255)
        self.QUIT_BUTTON_COLOUR = pygame.color.Color(233, 80, 80, 255)
        self.QUIT_BUTTON_HOVER_COLOUR = pygame.color.Color(213, 60, 60, 255)
        self.BUTTON_FONT_COLOUR = pygame.color.THECOLORS['black']


        # Fonts
        self.FONT = "./font/SourceSansPro-Regular.ttf"
        self.FONTSIZE = 2.2
        self.TIMER_FONTSIZE = 4.2
        self.BUTTON_FONTSIZE = 1.6
        self.MESSAGE_FONTSIZE = 3.0

        #Set Up Pygame Environment
        pygame.init()
        self.screen = pygame.display.set_mode([self.WIDTH,self.HEIGHT])
        pygame.display.set_caption("GoGo")
        
        #Create the players sidebars
        self.blackPlayer = UIPlayer(self.screen,self.screen,
                'Black',self.FONT,self.BASELINE_GRID,self.FONTSIZE,
                self.BLACKSTONE,self.WHITESTONE,
                0.2,1,True, self.TIMER_FONTSIZE,self.BUTTON_FONTSIZE,
                    self.PASS_BUTTON_COLOUR, self.PASS_BUTTON_HOVER_COLOUR, self.QUIT_BUTTON_COLOUR, self.QUIT_BUTTON_HOVER_COLOUR,
                    self.BUTTON_FONT_COLOUR,0,0,self.eventHandler)
        
        self.whitePlayer = UIPlayer(self.screen,self.screen,
                'White',self.FONT,self.BASELINE_GRID,self.FONTSIZE,
                self.WHITESTONE,self.BLACKSTONE,
                0.2,1,False,self.TIMER_FONTSIZE,self.BUTTON_FONTSIZE,
                    self.PASS_BUTTON_COLOUR, self.PASS_BUTTON_HOVER_COLOUR,self.QUIT_BUTTON_COLOUR,self.QUIT_BUTTON_HOVER_COLOUR,
                    self.BUTTON_FONT_COLOUR,0.8,0,self.eventHandler)
        
        self.board = UIGameBoard(self.screen,self.screen,"",self.FONT,
                                 self.BASELINE_GRID, self.FONTSIZE,
                                 self.BOARDCOLOUR,self.LINECOLOUR,
                                 0.6,self.WIDTH/self.HEIGHT*0.6,
                                 self.boardSize, 1, 0.2, 0.06)
        
        self.stones = UIStones([["B"],["W"]], self.screen, self.board,
                             '',self.FONT, self.BASELINE_GRID, self.FONTSIZE,
                             self.WHITESTONE, self.BLACKSTONE,1,1,self.board)
        
        self.cursor = UICursor(self.board,self.screen, self.QUIT_BUTTON_COLOUR)        
    
        self.winScreen = UIMessage(self.screen, self.screen,
                            "",
                            self.FONT,self.BASELINE_GRID,self.MESSAGE_FONTSIZE,
                            pygame.color.Color(0,0,0,60),self.WHITESTONE,0.8,0.7,
                            self.BUTTON_FONTSIZE, self.BUTTON_FONT_COLOUR,
                            self.PASS_BUTTON_COLOUR,self.PASS_BUTTON_HOVER_COLOUR,
                            "New Game",None, 0.1,0.15, self.eventHandler)

    def update(self, stoneMatrix, activePlayer, blackTime, whiteTime, blackPrisoners,whitePrisoners, cursorPos):
        whiteTimeStr = "{} : {:02d}".format(whiteTime//60,whiteTime%60)
        self.whitePlayer.timer.update(whiteTimeStr)
        blackTimeStr = "{} : {:02d}".format(blackTime//60,blackTime%60)
        self.blackPlayer.timer.update(blackTimeStr)
        whitePrisonersStr = "Prisoners = {}".format(whitePrisoners)
        self.whitePlayer.prisoners.update(whitePrisonersStr)
        blackPrisonersStr = "Prisoners = {}".format(blackPrisoners)
        self.blackPlayer.prisoners.update(blackPrisonersStr)
        

        if activePlayer == 0:
            self.blackPlayer.isActive = True
            self.whitePlayer.isActive = False
        elif activePlayer == 1:
            self.blackPlayer.isActive = False
            self.whitePlayer.isActive = True
        
        self.screen.fill(self.BOARDCOLOUR)
        self.blackPlayer.update()
        self.whitePlayer.update()
        self.board.update()
        self.stones.setStones(stoneMatrix)
        self.stones.update()
        self.cursor.coordinates = cursorPos
        self.cursor.draw()
        pygame.display.update()

    def drawEnd(self, text):
        self.winScreen.text = text
        self.winScreen.update()
        pygame.display.update()
        
    def quit(self):
        pygame.quit()
