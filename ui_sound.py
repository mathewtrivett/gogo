import pygame, os, random

class UISound():
    def __init__(self, soundsDirectory):
        pygame.mixer.init()
        self.soundsDirectory = soundsDirectory

    def update(self):
        self.file = random.choice(os.listdir(self.soundsDirectory))
        self.sound = pygame.mixer.Sound(self.soundsDirectory + self.file)
        self.sound.play()
