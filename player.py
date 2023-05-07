"""
    Player character
"""
import pygame
import globals

class Player:
    def __init__(self) -> None:
        self.image = pygame.image.load('img/player.png')
        self.rect = self.image.get_rect(topleft=(200, 200), size=(150, 200))

    def input(self, keys):
        pass

    def update(self):
        pass

    def draw(self):
        globals.window.blit(self.image, self.rect)
