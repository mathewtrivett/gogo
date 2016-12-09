import pygame

class EventHandler():
    
    def __init__(self):
        self.DECREMENTCLOCK = pygame.USEREVENT+1
        pygame.time.set_timer(self.DECREMENTCLOCK, 1000)

    def update(self):
        self.events = pygame.event.get()
    
    def keyWasPressed(self,keyCode):
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == keyCode:
                    return True
        return False
    
    def getTimePassed(self):
        time = 0
        for event in self.events:
            if event.type == self.DECREMENTCLOCK:
                time += 1
        return time
    
    def hasQuit(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                return True
        return False
    
    def leftClicked(self):
        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN and \
                event.button == 1:
                return True
        return False
