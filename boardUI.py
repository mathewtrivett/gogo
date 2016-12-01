import pygame
import pygame.gfxdraw

## SIZE VARIABLES
WIDTH = 800
HEIGHT = 600
FRAMERATE = 60
BOARD_SIZE = WIDTH * 0.60

## Colours and Textures
BG = pygame.color.THECOLORS['grey']
BOARDCOLOUR = pygame.color.THECOLORS['chocolate4']
LINECOLOUR = pygame.color.THECOLORS['black']
WHITESTONE = pygame.color.THECOLORS['linen']
BLACKSTONE = pygame.color.THECOLORS['black']

class Board_UI():
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
        self.coordinates = [[(y,x) for x in range(int(self.origin[0]), int(self.origin[0] + self.interval*self.grid), int(self.interval))] for y in range(int(self.origin[1]), int(self.origin[1] + self.interval*self.grid), int(self.interval))]

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

    def getBoardUICoords(self, coordinates):
        return self.coordinates[coordinates[0]][coordinates[1]]


class Stone_UI():
    
    def __init__(self, Board_UI, colour, coordinates):
        self.board = Board_UI
        self.diameter = Board_UI.interval - 3
        self.colour = colour
        self.coords = coordinates
        self.coordinates = tuple(map(lambda x,y: x+self.board.interval*y, self.board.origin, coordinates))

    def place(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.coordinates[1]),int(self.coordinates[0])),
                           int(self.diameter/2))

    def aa(self):
        pygame.gfxdraw.aacircle(screen,
                                int(self.coordinates[1]),
                                int(self.coordinates[0]),
                                int(self.diameter/2),
                                self.colour)
        
        pygame.gfxdraw.filled_circle(screen,
                                int(self.coordinates[1]),
                                int(self.coordinates[0]),
                                int(self.diameter/2),
                                self.colour)

        print(self.coors, int(self.coordinates[0]), int(self.coordinates[1]))

    def remove(self):
        pass


              
class Button_UI():
    pass


class Timer_UI():
    pass



class Player_UI():
    pass



pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
title = pygame.display.set_caption("GoGo")
screen.fill(BG)
pygame.display.flip()

while True:
    event = pygame.event.poll()
    board = Board_UI(12)
    board.show()
    black_stone = Stone_UI(board,BLACKSTONE,(2,4))
    black_stone.aa()
    white_stone = Stone_UI(board,WHITESTONE,(0,3))
    white_stone.aa()
    white_stone = Stone_UI(board,WHITESTONE,(1,3))
    white_stone.aa()
    white_stone = Stone_UI(board,WHITESTONE,(1,2))
    white_stone.aa()
    pygame.display.update()
    
    if event.type == pygame.QUIT :
        break
pygame.quit()
