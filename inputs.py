import pygame

class Inputs():
    
    def __init__(self):
        self.update()
        pygame.init()
        pygame.display.set_mode((100, 100))
        while True:
            keysPressed = pygame.key.get_pressed()
            print(keysPressed)
            if keysPressed[pygame.K_a]:
                print(a)

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
