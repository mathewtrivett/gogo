import pygame
import pygame.gfxdraw
from stoneUI import StoneUI
from buttonUI import ButtonUI

## SIZE VARIABLES
WIDTH = 1024
HEIGHT = 768
FRAMERATE = 60
BOARD_SIZE = WIDTH * 0.60

## Colours and Textures
BG = pygame.color.THECOLORS['grey']
BOARDCOLOUR = pygame.color.THECOLORS['chocolate4']
LINECOLOUR = pygame.color.THECOLORS['black']
WHITESTONE = pygame.color.THECOLORS['antiquewhite1']
BLACKSTONE = pygame.color.THECOLORS['grey10']
BUTTONCOLOUR = pygame.color.THECOLORS['aquamarine3']
BUTTONFONT = "/Library/Fonts/SourceSansPro-Regular.ttf"

class BoardUI():
    global screen
    global WIDTH
    global LINECOLOUR
        
    def __init__(self, grid, lineWidth=1):
        self.grid = grid
        self.divisor = grid + 1
        self.bg = pygame.draw.rect(screen, BOARDCOLOUR, (WIDTH * 0.2, WIDTH* 0.05, BOARD_SIZE, BOARD_SIZE))
        self.interval = self.bg.width / self.divisor # Divides the background by the divisor
        self.lineWidth = lineWidth # Sets the grid's line width
        self.origin = (self.bg.y + self.interval, self.bg.x + self.interval)
        self.farCorner = tuple(map(lambda x,y: x+self.interval*y, self.origin, (self.grid,self.grid)))
        self.coordinates = [[(x,y) for x in range(int(self.origin[0]), int(self.farCorner[0]), int(self.interval))] for y in range(int(self.origin[1]), int(self.farCorner[1]), int(self.interval))]

    def show(self):       
        for position in range(self.divisor):
                if position == 0:
                    continue

                # Horizontal Grid
                pygame.draw.line(screen,
                             LINECOLOUR,
                             (self.bg.x + self.interval, self.bg.y + self.interval * position),
                             (self.bg.x + self.bg.width - self.interval, self.bg.y + self.interval * position),
                             self.lineWidth)
                
                # Vertical Grid
                pygame.draw.line(screen,
                                 LINECOLOUR,
                                 (self.bg.x + self.interval * position, self.bg.y + self.interval),
                                 (self.bg.x + self.interval * position, self.bg.height + self.bg.y - self.interval),
                                 self.lineWidth)

    def returnCoords(self, pixelCoords):
        return self.coordinates[pixelCoords[0]][pixelCoords[1]]



pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
title = pygame.display.set_caption("GoGo")
screen.fill(BG)
pygame.display.flip()
passbutton = ButtonUI(screen,"Pass", BUTTONCOLOUR, BUTTONFONT, 24, BLACKSTONE,
                  (20,20),"None")

quitbutton = ButtonUI(screen,"Quit", BUTTONCOLOUR, BUTTONFONT, 24, BLACKSTONE,
                  (100,20),"None")

while True:
    event = pygame.event.poll()
    board = BoardUI(9) 
    board.show()
    passbutton.draw()
    quitbutton.draw()
    black_stone = StoneUI(board,BLACKSTONE,(1,1),screen)
    black_stone.show()
    black_stone.move(1,1)
    white_stone = StoneUI(board,WHITESTONE,(0,3),screen)
    white_stone.show()
    white_stone = StoneUI(board,WHITESTONE,(1,3),screen)
    white_stone.show()
    white_stone = StoneUI(board,WHITESTONE,(18,18),screen)
    white_stone.show()
    pygame.display.update()
    
    if event.type == pygame.QUIT :
        break

pygame.quit()
