import pygame

class EventHandler():
    
    def __init__(self):
        self.DECREMENTCLOCK = pygame.USEREVENT+1
        pygame.time.set_timer(self.DECREMENTCLOCK, 1000)
        self.update()
        
    def update(self):
        self.events = pygame.event.get()
        
    def keyIsDown(self,keyCode):
        keysPressed = pygame.key.get_pressed()
        return keysPressed[keyCode]
    
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
