import pygame
import pygame.gfxdraw
from stone import Stone
# from button import Button
from gameboard import GameBoard
from element import Element

WIDTH = 640
HEIGHT = 480
FRAMERATE = 60
BASELINE_GRID = WIDTH / 64

## Colours and Textures
BG = pygame.color.THECOLORS['grey']
BOARDCOLOUR = pygame.color.THECOLORS['chocolate4']
LINECOLOUR = pygame.color.THECOLORS['black']
WHITESTONE = pygame.color.THECOLORS['antiquewhite1']
BLACKSTONE = pygame.color.THECOLORS['grey10']
PASS_BUTTON_COLOUR = pygame.color.THECOLORS['aquamarine3']
QUIT_BUTTON_COLOUR = pygame.color.Color(233, 80, 80, 255)
BUTTONFONT = "/Library/Fonts/SourceSansPro-Regular.ttf"

## SETUP Pygame Environment
pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
title = pygame.display.set_caption("GoGo")

screen.fill(BG)
board = GameBoard(9,0.6,LINECOLOUR,1,BOARDCOLOUR,screen)
pygame.display.flip()

all_stones = pygame.sprite.Group()
white_stone = Stone(board,WHITESTONE,screen)
all_stones.add(white_stone)

## Player Areas
pygame.draw.rect(screen,BLACKSTONE,(0,0,WIDTH * 0.2, HEIGHT)) # Player area 
pygame.draw.rect(screen,WHITESTONE,(WIDTH - WIDTH * 0.2,0,WIDTH,HEIGHT)) # Player area

whitePlayer = pygame.draw.rect(screen,WHITESTONE,(0,0,WIDTH * 0.2, HEIGHT * 0.18)) # (surface, opponentColour, parent.x,parent.y, parent.bottomright,% of parent height as variable) 
blackPlayer = pygame.draw.rect(screen,BLACKSTONE,(WIDTH - WIDTH * 0.2,0,WIDTH,HEIGHT*0.18)) # (surface, opponentColour, parent.x, parent.y, parent.bottomright,% of parent height as variable)

## Fonts
font = pygame.font.Font(BUTTONFONT, int(BASELINE_GRID*2.2)) # (Font, Fontsize)
timer = pygame.font.Font(BUTTONFONT, int(BASELINE_GRID*4.2)) # (Font, Fontsize)
button_text = pygame.font.Font(BUTTONFONT,int(BASELINE_GRID*1.6)) # (Font, Fontsize)

black_time = timer.render("3:00",True,BLACKSTONE) # Timer value
white_time = timer.render("2:14",True, WHITESTONE) # Timer value
timer_size = timer.size("3:00") # Timer.size
black = font.render("Black", True, BLACKSTONE) # Player Colour, player.colour
white = font.render("White", True, WHITESTONE) # Player Colour, player.colour
black_size = font.size("Black")
white_size = font.size("White")


# Player names
screen.blit(black,(blackPlayer.width/2-black_size[0]/2,blackPlayer.height-black_size[1])) # self.screen.blit(self.text, self.width
screen.blit(white,(int(WIDTH-WIDTH * 0.2 + (white_size[0]/2)),whitePlayer.height-white_size[1])) # self.screen.blit(self.text, self.parent.x - self.text.size[0]/2,parent.height-self.text.size[1])

# Timers
screen.blit(black_time,(blackPlayer.width/2-timer_size[0]/2,0)) # self.screen(self.text, self.parent.width/2-self.text.size[0]/2,self.y)
screen.blit(white_time,(WIDTH - WIDTH * 0.2+whitePlayer.width/2-timer_size[0]/2,0))

# black_pass = ButtonUI(screen,)

test = Element(screen,screen,"topright","",WHITESTONE,BLACKSTONE,"d",0,0,0.3,0.5)
test.draw()

while True:
    event = pygame.event.poll()
    pygame.display.update()
    
    ## Update
    all_stones.update()
    all_stones.draw(screen)
    if event.type == pygame.QUIT :
        break   
pygame.quit()
