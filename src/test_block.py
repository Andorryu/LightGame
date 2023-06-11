
import pygame
from entity import Entity
from utils.vector import Vector
import globals
import utils.colors as colors
from utils.collider import Collider
from game_platform import Platform

class Block(Entity):
    def __init__(self) -> None:
        # physics
        self.pos = globals.game_space/2
        self.velocity = Vector(0, 0)
        self.speed = 70
        # collider
        self.collider = Collider(
            pos = self.pos,
            size = Vector(1000, 1000)
        )
        # image
        self.surf = pygame.Surface(self.collider.size.compat())
        # controls
        self.moveleft, self.moveright, self.moveup, self.movedown = False, False, False, False
    
    def input(self, keys):
        self.moveup, self.moveright, self.movedown, self.moveleft = keys[pygame.K_w], keys[pygame.K_d], keys[pygame.K_s], keys[pygame.K_a]

    def update(self, platforms: list[Platform]):

        # update physics
        self.velocity = Vector(0, 0)
        if self.moveup:
            self.velocity.y = -self.speed
        if self.moveright:
            self.velocity.x = self.speed
        if self.movedown:
            self.velocity.y = self.speed
        if self.moveleft:
            self.velocity.x = -self.speed
        self.pos += self.velocity

        for pf in platforms:
            self.pos = self.collider.update_hard_collision(self.pos, pf.collider)


    def draw(self):
        self.surf.fill(colors.GREEN)
        rect = self.surf.get_rect(center=self.pos.compat())
        globals.window.blit(self.surf, rect)
