
import pygame
from entity import Entity
from utils.vector import Vector
import globals
import utils.colors as colors

class Block(Entity):
    def __init__(self) -> None:
        self.pos = globals.game_space/2
        self.velocity = Vector(0, 0)
        self.speed = 70
        self.moveleft, self.moveright, self.moveup, self.movedown = False, False, False, False
        self.size = Vector(1000, 1000)
        self.img = pygame.Surface(self.size.compat())
    
    def input(self, keys):
        self.moveup, self.moveright, self.movedown, self.moveleft = keys[pygame.K_w], keys[pygame.K_d], keys[pygame.K_s], keys[pygame.K_a]

    def update(self, colliders):
        last_pos = self.pos # position from last frame

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

        # test if overlapping:
        

    def draw(self):
        self.img.fill(colors.GREEN)
        self.rect = self.img.get_rect(center=self.pos.compat())
        globals.window.blit(self.img, self.rect)
