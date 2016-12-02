import pygame
import pygame.gfxdraw
from stone import Stone
from buttonUI import ButtonUI
from gameboard import GameBoard

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

## SETUP Pygame Environment
pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
title = pygame.display.set_caption("GoGo")
screen.fill(BG)
pygame.display.flip()

board = GameBoard(19,0.6,LINECOLOUR,1,BOARDCOLOUR,screen)
black_stone = Stone(board,BLACKSTONE,(0,0),screen)
white_stone = Stone(board,WHITESTONE,(1,0),screen)

while True:
    event = pygame.event.poll()
    ## Update
    pygame.display.update()
    black_stone.move()
    
    if event.type == pygame.QUIT :
        break
    
pygame.quit()
