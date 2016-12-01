import pygame
import pygame.gfxdraw
from stoneUI import StoneUI
from buttonUI import ButtonUI
from boardUI import BoardUI

## SIZE VARIABLES
WIDTH = 1024
HEIGHT = 768
FRAMERATE = 60

## Colours and Textures
BG = pygame.color.THECOLORS['grey']
BOARDCOLOUR = pygame.color.THECOLORS['chocolate4']
LINECOLOUR = pygame.color.THECOLORS['black']
WHITESTONE = pygame.color.THECOLORS['antiquewhite1']
BLACKSTONE = pygame.color.THECOLORS['grey10']
BUTTONCOLOUR = pygame.color.THECOLORS['aquamarine3']
BUTTONFONT = "/Library/Fonts/SourceSansPro-Regular.ttf"
BLACKIMG = "./img/Black.png"
WHITEIMG = "./img/White.png"


## SETUP Pygame Environment
pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
title = pygame.display.set_caption("GoGo")
screen.fill(BG)

# Initialise Board
board = BoardUI(12,0.6,1,LINECOLOUR,BOARDCOLOUR, screen)
board.draw()
black_stone = StoneUI(board,"Black",BLACKIMG,(0,0),screen)
black_stone.draw()


# Buttons

passbutton = ButtonUI(screen,"Pass", BUTTONCOLOUR, BUTTONFONT, 24, BLACKSTONE,
                  (20,20),"None")

quitbutton = ButtonUI(screen,"Quit", BUTTONCOLOUR, BUTTONFONT, 24, BLACKSTONE,
                  (100,20),"None")

pygame.display.flip()


while True:
    event = pygame.event.poll()
    passbutton.draw()
    quitbutton.draw()
    black_stone.move(3,1)
    # black_stone.move(-1,-1)
    white_stone = StoneUI(board,"White",WHITEIMG,(0,3),screen)
    white_stone.draw()
    white_stone = StoneUI(board,"White",WHITEIMG,(1,3),screen)
    white_stone.draw()
    white_stone = StoneUI(board,"White",WHITEIMG,(18,18),screen)
    white_stone.draw()
    pygame.display.update()
    
    if event.type == pygame.QUIT :
        break

pygame.quit()
