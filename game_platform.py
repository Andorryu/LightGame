"""

"""
import pygame
from utils.vector import Vector
import globals
import utils.colors as colors
from entity import Entity

class Platform(Entity):
    def __init__(self, pos: Vector=None, size: Vector=Vector(12000, 1000)) -> None:
        if pos == None:
            self.pos = globals.game_space/2 + Vector(0, 3500)
        else:
            self.pos = pos
        self.size = size
        self.surf = pygame.Surface(size.compat())
        self.rect = self.surf.get_rect(center=self.pos.compat())

    def draw(self):
        self.surf.fill(colors.WHITE)
        globals.window.blit(self.surf, self.rect)