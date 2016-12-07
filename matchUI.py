import pygame
import pygame.gfxdraw
from stone import Stone
from button import Button
from gameboard import GameBoard
from element import Element
from player_ui import Player
from timer import Timer

WIDTH = 1024
HEIGHT = 768
FRAMERATE = 60
BASELINE_GRID = WIDTH / 64
ACTIVE_PLAYER_OUTLINE = int(BASELINE_GRID/3)

## Colours and Textures
BG = pygame.color.THECOLORS['grey']
BOARDCOLOUR = pygame.color.THECOLORS['chocolate4']
LINECOLOUR = pygame.color.THECOLORS['black']
WHITESTONE = pygame.color.THECOLORS['antiquewhite1']
BLACKSTONE = pygame.color.THECOLORS['grey10']
PASS_BUTTON_COLOUR = pygame.color.THECOLORS['aquamarine3']
QUIT_BUTTON_COLOUR = pygame.color.Color(233, 80, 80, 255)


# Fonts
FONT = "./font/SourceSansPro-Regular.ttf"
FONTSIZE = 2.2
TIMER_FONTSIZE = 4.2
BUTTON_FONTSIZE = 1.6

## SETUP Pygame Environment
pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
title = pygame.display.set_caption("GoGo")

screen.fill(BOARDCOLOUR)
board = GameBoard(9,0.6,LINECOLOUR,1,BOARDCOLOUR,screen)
pygame.display.flip()

all_stones = pygame.sprite.Group()
white_stone = Stone(board,WHITESTONE,screen)
all_stones.add(white_stone)


## Black's UI Elements
black = Player(screen,screen,'topleft',
                'Black',FONT,BASELINE_GRID,FONTSIZE,
                BLACKSTONE,WHITESTONE,
                0.2,1,False)

black.draw()
black.positionText(0.5,0.24)
black.setActive(ACTIVE_PLAYER_OUTLINE)

## Timer
blackTimer = Timer(screen,black,'topleft',
              "3:00",FONT,BASELINE_GRID,TIMER_FONTSIZE,
              BLACKSTONE,WHITESTONE,
              1,0.2)
blackTimer.draw()
blackTimer.positionText(0.5,1)

## Buttons
bPassButton = Button(screen,black,'topleft',
                    'Pass',FONT,BASELINE_GRID,BUTTON_FONTSIZE,
                    PASS_BUTTON_COLOUR,BLACKSTONE,
                    0.5,0.06,"Pass")

bQuitButton = Button(screen,black,'topright',
                    'Resign',FONT,BASELINE_GRID,BUTTON_FONTSIZE,
                    QUIT_BUTTON_COLOUR,BLACKSTONE,
                    0.5,0.06,"Resign")
bPassButton.draw()
bPassButton.positionText(0.5,0.5)
bQuitButton.draw()
bPassButton.onClick()
bQuitButton.positionText(0.5,0.5)
bQuitButton.onClick()


## White's UI Elements
white = Player(screen,screen,'topright',
                'White',FONT,BASELINE_GRID,FONTSIZE,
                WHITESTONE,BLACKSTONE,
                0.2,1,True)

white.draw()
white.positionText(0.5,0.24)
white.setActive(ACTIVE_PLAYER_OUTLINE)

## Timer
whiteTimer = Timer(screen,white,'topleft',
              "2:10",FONT,BASELINE_GRID,TIMER_FONTSIZE,
              WHITESTONE,BLACKSTONE,
              1,0.2)
whiteTimer.draw()
whiteTimer.update("1:38")
whiteTimer.positionText(0.5,1)


## Buttons
wPassButton = Button(screen,white,'topleft',
                    'Pass',FONT,BASELINE_GRID,BUTTON_FONTSIZE,
                    PASS_BUTTON_COLOUR,BLACKSTONE,
                    0.5,0.06,"Resign")
wQuitButton = Button(screen,white,'topright',
                    'Resign',FONT,BASELINE_GRID,BUTTON_FONTSIZE,
                    QUIT_BUTTON_COLOUR,BLACKSTONE,
                    0.5,0.06,"Resign")

wPassButton.draw()
wPassButton.positionText(0.5,0.5)
wQuitButton.draw()
wQuitButton.positionText(0.5,0.5)
wPassButton.onClick()
wQuitButton.onClick()


while True:
    event = pygame.event.poll()
    pygame.display.update()
    wPassButton.onHover()
    wQuitButton.onHover()
    wPassButton.onClick()
    
    
    ## Update
    all_stones.update()
    all_stones.draw(screen)
    if event.type == pygame.QUIT :
        break   
pygame.quit()
