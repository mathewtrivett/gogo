import pygame

WIDTH = 1024
HEIGHT = 768
FRAMERATE = 60
BOARDCOLOUR = pygame.color.THECOLORS['chocolate4']
BG = pygame.color.THECOLORS['linen']

class Board():
    
    def __init__(self):
        pass

    '''
    Loop through a nested range up to the board size
    For each, draw a line of a fixed length, offset by the correct amount.
    '''
    def show(self):
        global screen
        BOARD_SIZE = WIDTH // 5 * 3
        background = pygame.draw.rect(screen, BOARDCOLOR)
        background.center
        pass

class Button():
    pass


class Timer():
    pass


class Stone():
    pass


class Player():
    pass


class CapturedStone(Stone):
    pass


pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT],pygame.RESIZABLE)
title = pygame.display.set_caption("GoGo")
screen.fill(BG)
pygame.display.flip()


while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT :
        break
pygame.quit()
