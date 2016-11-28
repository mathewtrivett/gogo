import pygame

WIDTH = 1024
HEIGHT = 768
FRAMERATE = 60
BOARDCOLOUR = pygame.color.THECOLORS['chocolate4']
BG = pygame.color.THECOLORS['linen']
LINECOLOUR = pygame.color.THECOLORS['black']
BOARD_SIZE = WIDTH * 0.60
WHITESTONE = pygame.color.THECOLORS['linen']
BLACKSTONE = pygame.color.THECOLORS['black']

class Board_UI():
    global screen
    global WIDTH
    global LINECOLOUR
        
    def __init__(self, grid, lineWidth=1):
        self.grid = grid
        self.divisor = self.grid + 1
        self.bg = pygame.draw.rect(screen, BOARDCOLOUR, (WIDTH * 0.2, WIDTH* 0.05, BOARD_SIZE, BOARD_SIZE))
        self.interval = self.bg.width / self.divisor # Divides the background by the grid size + 1
        self.lineWidth = lineWidth # Sets the grid's line width

    def show(self):
        # Board Background
       
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

               
class Button_UI():
    pass


class Timer_UI():
    pass


class Stone_UI():

    def __init__(self, Board_UI, colour, coordinates):
        self.board = Board_UI
        self.diameter = Board_UI.interval - 3
        self.colour = colour
        self.coordinates = coordinates

    def show(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.board.bg.x + self.board.bg.width/2),int(self.board.bg.y + self.board.bg.height/2)),
                           int(self.diameter/2))

class Player_UI():
    pass

class CapturedStone_UI(Stone_UI):
    pass

pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
title = pygame.display.set_caption("GoGo")
screen.fill(BG)
pygame.display.flip()

while True:
    event = pygame.event.poll()
    board = Board_UI(9)
    board.show()
    black_stone = Stone_UI(board,BLACKSTONE,(0,0))
    black_stone.show()
    white_stone = Stone_UI(board,WHITESTONE,(3,3))
    white_stone.show()
    pygame.display.update()
    
    if event.type == pygame.QUIT :
        break
pygame.quit()
