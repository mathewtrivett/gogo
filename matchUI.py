import pygame
import pygame.gfxdraw
from stone import Stone
from button import Button
from gameboard import GameBoard
from element import Element

WIDTH = 1024
HEIGHT = 768
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


# Fonts
FONT = "./font/SourceSansPro-Regular.ttf"
FONTSIZE = 2.2
TIMER_FONTSIZE = 4.2
BUTTON_FONTSIZE = 1.6

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


## UI Elements
black = Element(screen,screen,'topleft',
                'Black',FONT,BASELINE_GRID,FONTSIZE,
                BLACKSTONE,WHITESTONE,
                0,0,0.2,1)

white = Element(screen,screen,'topright',
                'White',FONT,BASELINE_GRID,FONTSIZE,
                WHITESTONE,BLACKSTONE,
                0,0,0.2,1)
black.draw()
black.positionText(0.5,0.24)
white.draw()
white.positionText(0.5,0.24)

bPassButton = Button(screen,black,'topleft',
                    'Pass',FONT,BASELINE_GRID,BUTTON_FONTSIZE,
                    PASS_BUTTON_COLOUR,BLACKSTONE,
                    0,0,0.5,0.06,"Pass")
bQuitButton = Button(screen,black,'topright',
                    'Quit',FONT,BASELINE_GRID,BUTTON_FONTSIZE,
                    QUIT_BUTTON_COLOUR,BLACKSTONE,
                    0,0,0.5,0.06,"Quit")

bPassButton.draw()
bPassButton.positionText(0.5,0.5)
bQuitButton.draw()
bPassButton.onClick()
bQuitButton.positionText(0.5,0.5)
bQuitButton.onClick()

wPassButton = Button(screen,white,'topleft',
                    'Pass',FONT,BASELINE_GRID,BUTTON_FONTSIZE,
                    PASS_BUTTON_COLOUR,BLACKSTONE,
                    0,0,0.5,0.06,"Pass")
wQuitButton = Button(screen,white,'topright',
                    'Quit',FONT,BASELINE_GRID,BUTTON_FONTSIZE,
                    QUIT_BUTTON_COLOUR,BLACKSTONE,
                    0,0,0.5,0.06,"Quit")

wPassButton.draw()
wPassButton.positionText(0.5,0.5)
wQuitButton.draw()
wQuitButton.positionText(0.5,0.5)
wPassButton.onClick()
wQuitButton.onClick()

##black_time = timer.render("3:00",True,BLACKSTONE) # Timer value
##white_time = timer.render("2:14",True, WHITESTONE) # Timer value
##timer_size = timer.size("3:00") # Timer.size
##black = font.render("Black", True, BLACKSTONE) # Player Colour, player.colour
##white = font.render("White", True, WHITESTONE) # Player Colour, player.colour
##black_size = font.size("Black")
##white_size = font.size("White")


# Player names
#screen.blit(black,(blackPlayer.width/2-black_size[0]/2,blackPlayer.height-black_size[1])) # self.screen.blit(self.text, self.width
#screen.blit(white,(int(WIDTH-WIDTH * 0.2 + (white_size[0]/2)),whitePlayer.height-white_size[1])) # self.screen.blit(self.text, self.parent.x - self.text.size[0]/2,parent.height-self.text.size[1])

# Timers
#screen.blit(black_time,(blackPlayer.width/2-timer_size[0]/2,0)) # self.screen(self.text, self.parent.width/2-self.text.size[0]/2,self.y)
#screen.blit(white_time,(WIDTH - WIDTH * 0.2+whitePlayer.width/2-timer_size[0]/2,0))


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
