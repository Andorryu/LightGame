"""

"""
import pygame
from utils.vector import Vector
import globals
import utils.colors as colors

class Platform:
    def __init__(self, pos: Vector=None, size: Vector=Vector(12000, 1000)) -> None:
        if pos == None:
            pos = globals.game_space/2 + Vector(0, 3500)
        self.surf = pygame.Surface(size.compat())
        self.rect = self.surf.get_rect(center=pos.compat())

    def draw(self):
        self.surf.fill(colors.WHITE)
        globals.window.blit(self.surf, self.rect)