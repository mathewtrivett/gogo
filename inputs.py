import pygame

class Inputs():
    
    def __init__(self):
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
    
    def hasQuit(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                return True
        return False
