import pygame

class Inputs():
    
    def __init__(self):
        
        pygame.init()
        pygame.display.set_mode((100, 100))
        while True:
            keysPressed = pygame.key.get_pressed()
            print(keysPressed)
            if keysPressed[pygame.K_a]:
                print(a)
        
    def keyIsDown(self,keyCode):
        keysPressed = pygame.key.get_pressed()
        return keysPressed[keyCode]
    
    def keyWasPressed(self,keyCode):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == keyCode:
                    return True
        return False
    
    def hasQuit(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return True
        return False
    
i = Inputs()
