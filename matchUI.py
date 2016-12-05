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
board = GameBoard(9,0.6,LINECOLOUR,1,BOARDCOLOUR,screen)
pygame.display.flip()

all_stones = pygame.sprite.Group()
white_stone = Stone(board,WHITESTONE,screen)
all_stones.add(white_stone)

## Player Areas
pygame.draw.rect(screen,BLACKSTONE,(0,0,WIDTH * 0.2, HEIGHT))
pygame.draw.rect(screen,WHITESTONE,(WIDTH - WIDTH * 0.2,0,WIDTH,HEIGHT))
whitePlayer = pygame.draw.rect(screen,WHITESTONE,(0,0,WIDTH * 0.2, HEIGHT * 0.18))
blackPlayer = pygame.draw.rect(screen,BLACKSTONE,(WIDTH - WIDTH * 0.2,0,WIDTH,HEIGHT*0.18))

font = pygame.font.Font(BUTTONFONT, int(WIDTH/64*2.2))
timer = pygame.font.Font(BUTTONFONT, int(WIDTH/64*4.2))
black_time = timer.render("3:00",True,BLACKSTONE)
white_time = timer.render("2:14",True, WHITESTONE)
timer_size = timer.size("3:00")
black = font.render("Black", True, BLACKSTONE)
white = font.render("White", True, WHITESTONE)
black_size = font.size("Black")
white_size = font.size("White")

screen.blit(black,(blackPlayer.width/2-black_size[0]/2,blackPlayer.height-black_size[1]))
screen.blit(white,(int(WIDTH-WIDTH *0.2+(white_size[0]/2)),whitePlayer.height-white_size[1]))
screen.blit(black_time,(blackPlayer.width/2-timer_size[0]/2,0))
screen.blit(white_time,(WIDTH - WIDTH * 0.2+whitePlayer.width/2-timer_size[0]/2,0))

## Buttons

# pygame.draw.rect(screen,BUTTONCOLOUR, (0,0),)

while True:
    event = pygame.event.poll()
    pygame.display.update()
    ## Update
    all_stones.update()
    all_stones.draw(screen)
    if event.type == pygame.QUIT :
        break
    
pygame.quit()
