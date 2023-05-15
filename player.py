"""
    Player character
"""
import pygame
import globals
from vector import Vector

class Player:
    def __init__(self) -> None:
        self.image = pygame.image.load('img/player.png')
        self.size = Vector(250, 450)
        self.image = pygame.transform.scale(self.image, self.size.compatible())
        self.rect = self.image.get_rect(center=(200, 200), size=self.size.compatible())

    def input(self, keys):
        pass

    def update(self):
        pass

    def draw(self):
        globals.window.blit(self.image, self.rect)
