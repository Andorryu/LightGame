"""
    Player character
"""
import pygame
import globals
from utils.vector import Vector
from utils.animation import Animation
from utils.spritesheet import Spritesheet
from game_platform import Platform

class Ray:
    def __init__(self, p1: Vector, p2: Vector) -> None:
        self.p1 = p1
        self.p2 = p2

    def compat(self) -> tuple[tuple, tuple]:
        return self.p1.compat(), self.p2.compat()

class Player:
    
    SURF_RATIO = Vector(5, 9)
    RECT_RATIO = Vector(2, 9)
    LEFT = 0
    RIGHT = 1

    def __init__(self) -> None:
        # load animation and scale frames
        self.scale = 200
        self.surf_size = Player.SURF_RATIO*self.scale
        self.rect_size = Player.RECT_RATIO*self.scale
        self.idle_anim = Animation(Spritesheet("img/idle.png").slice(Vector(10, 1), self.surf_size), 1000*1)
        self.run_anim = Animation(Spritesheet("img/run.png").slice(Vector(3, 3), self.surf_size), 1000*.3)
        self.current_anim = self.idle_anim
        # position, speed, gravity
        self.pos = globals.game_space/2
        self.velocity = Vector(0, 0)
        self.speed = 70
        self.jump_speed = 100
        self.gravity = 5
        self.ray = Ray(self.pos + Vector(-self.rect_size.x/2, self.rect_size.y/2 + 10), self.pos + Vector(self.rect_size.x/2, self.rect_size.y/2 + 10))
        self.grounded = False
        self.stop_fall = False
        self.dir = Player.RIGHT
        # controls
        self.moveleft = False
        self.moveright = False
        self.jump = False

    def input(self, keys: pygame.key.ScancodeWrapper):
        self.moveleft = keys[pygame.K_a]
        self.moveright = keys[pygame.K_d]
        self.jump = keys[pygame.K_w] or keys[pygame.K_SPACE]

    def update(self):
        # create new rect every update for player movement(maybe this is optimizable?)
        self.rect = self.current_anim.current_frame.get_rect(center=self.pos.compat(), size=(self.rect_size).compat())
        # gravity
        if not self.grounded:
            self.velocity.y += self.gravity

        self.stop_fall = globals.edge_trigger(self.grounded, self.stop_fall)
        if self.stop_fall:
            self.velocity.y = 0

        # move left and right
        if self.moveleft:
            self.velocity.x = -self.speed
            self.current_anim = self.run_anim
            self.dir = Player.LEFT
        elif self.moveright:
            self.velocity.x = self.speed
            self.current_anim = self.run_anim
            self.dir = Player.RIGHT
        else:
            self.current_anim = self.idle_anim
            self.velocity.x = 0
        # jump
        if self.grounded and self.jump:
            self.velocity.y -= self.jump_speed

        # update position
        self.pos += self.velocity
        self.ray.p1 += self.velocity # ray stays under player
        self.ray.p2 += self.velocity

        # update animation frame
        self.current_anim.update()

    def draw(self):
        if self.dir == Player.LEFT:
            globals.window.blit(pygame.transform.flip(self.current_anim.current_frame, True, False), self.rect)
        else:
            globals.window.blit(self.current_anim.current_frame, self.rect)

    def check_platform_collision(self, platforms: list[Platform]):
        self.grounded = False
        for platform in platforms:
            if platform.rect.clipline(self.ray.compat()):
                self.grounded = True
