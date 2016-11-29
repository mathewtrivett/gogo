class Stone_UI():
    
    def __init__(self, Board_UI, colour, coordinates):
        self.board = Board_UI
        self.diameter = Board_UI.interval - 3
        self.colour = colour
        self.coordinates = tuple(map(lambda x,y: x+self.board.interval*y, self.board.origin, coordinates))

    def show(self):
        pygame.draw.circle(screen,
                           self.colour,
                           (int(self.coordinates[1]),int(self.coordinates[0])),
                           int(self.diameter/2))


from boardUI import Board_UI
