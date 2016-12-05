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
# black_stone = Stone(board,BLACKSTONE,screen)
screen.fill(BG)
board = GameBoard(19,0.6,LINECOLOUR,1,BOARDCOLOUR,screen)
pygame.display.flip()

all_stones = pygame.sprite.Group()

white_stone = Stone(board,WHITESTONE,screen)
all_stones.add(white_stone)
# all_stones.add(black_stone)

pygame.draw.rect(screen,BLACKSTONE,(0,0,int(WIDTH * 0.2), HEIGHT))
pygame.draw.rect(screen,WHITESTONE,(WIDTH - int(WIDTH * 0.2),0,WIDTH,HEIGHT))

while True:
    event = pygame.event.poll()
    pygame.display.update()
    ## Update
    all_stones.update()
    all_stones.draw(screen)

    if event.type == pygame.QUIT :
        break
    
pygame.quit()
