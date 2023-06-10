"""

"""
import pygame
from utils.vector import Vector
import globals
import utils.colors as colors
from entity import Entity
from utils.collider import Collider

class Platform(Entity):
    def __init__(self, pos: Vector=None, size: Vector=Vector(12000, 1000)) -> None:
        if pos == None:
            self.pos = globals.game_space/2 + Vector(0, 3500)
        else:
            self.pos = pos

        self.collider = Collider(self.pos, size)
        self.surf = pygame.Surface(size.compat())

    def draw(self):
        self.surf.fill(colors.ORANGE)
        rect = self.surf.get_rect(center=self.pos.compat())
        globals.window.blit(self.surf, rect)
