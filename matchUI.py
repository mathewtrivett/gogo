import pygame
import pygame.gfxdraw
from stone import Stone
# from buttonUI import ButtonUI
from gameboard import GameBoard

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
pass_Button = button_text.render("PASS",True,BLACKSTONE) # Button Text
quit_Button = button_text.render("RESIGN",True,BLACKSTONE) # Button Text
pass_size = button_text.size("PASS")
quit_size = button_text.size("RESIGN")

screen.blit(black,(blackPlayer.width/2-black_size[0]/2,blackPlayer.height-black_size[1])) # self.screen.blit(self.text, self.width
screen.blit(white,(int(WIDTH-WIDTH *0.2+(white_size[0]/2)),whitePlayer.height-white_size[1]))
screen.blit(black_time,(blackPlayer.width/2-timer_size[0]/2,0))
screen.blit(white_time,(WIDTH - WIDTH * 0.2+whitePlayer.width/2-timer_size[0]/2,0))

## Buttons

black_pass = pygame.draw.rect(screen,PASS_BUTTON_COLOUR, (0,whitePlayer.height,whitePlayer.width/2,HEIGHT*0.05))
white_pass = pygame.draw.rect(screen,PASS_BUTTON_COLOUR,(blackPlayer.x,blackPlayer.height,blackPlayer.width/2,HEIGHT*0.05))
black_quit = pygame.draw.rect(screen,QUIT_BUTTON_COLOUR,(black_pass.width,blackPlayer.height,WIDTH*0.2/2,HEIGHT*0.05))
white_quit = pygame.draw.rect(screen,QUIT_BUTTON_COLOUR,(WIDTH-white_pass.width,whitePlayer.height,WIDTH,HEIGHT*0.05))

screen.blit(pass_Button,(black_pass.x + black_pass.width/2-pass_size[0]/2,blackPlayer.height+black_pass.height/2-pass_size[1]/2))
screen.blit(pass_Button,(white_pass.x+white_pass.width/2-pass_size[0]/2,whitePlayer.height + white_pass.height/2-pass_size[1]/2))
screen.blit(quit_Button,(black_quit.x + black_quit.width/2-quit_size[0]/2,blackPlayer.height+black_quit.height/2-quit_size[1]/2))
screen.blit(quit_Button,(white_quit.x + white_quit.width/2-quit_size[0]/2,whitePlayer.height+white_quit.height/2-quit_size[1]/2))

while True:
    event = pygame.event.poll()
    pygame.display.update()
    ## Update
    all_stones.update()
    all_stones.draw(screen)
    if event.type == pygame.QUIT :
        break   
pygame.quit()
