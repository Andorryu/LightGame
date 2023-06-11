"""
    Player character
""" 
import pygame
import globals
from utils.vector import Vector
from utils.animation import Animation
from utils.spritesheet import Spritesheet
from game_platform import Platform
from entity import Entity
from utils.collider import Collider
from utils.physics import Physics

class Player(Entity):
    
    SURF_RATIO = Vector(5, 9)
    RECT_RATIO = Vector(2, 9)
    SCALE = 200
    LEFT = 0
    RIGHT = 1

    def __init__(self) -> None:
        # load animation and scale frames
        self.surf_size = Player.SURF_RATIO*Player.SCALE
        self.idle_anim = Animation(Spritesheet("img/idle.png").slice(Vector(10, 1), self.surf_size), 1000*1)
        self.run_anim = Animation(Spritesheet("img/run.png").slice(Vector(3, 3), self.surf_size), 1000*.3)
        self.current_anim = self.idle_anim
        # position, speed, gravity
        self.physics = Physics(
            pos = globals.game_space/2,
            velocity = Vector(0, 0),
            acceleration = (0, 5)
        )
        self.collider = Collider(
            pos = self.physics.pos,
            size = Player.RECT_RATIO*Player.SCALE
        )
        self.run_speed = 70
        self.jump_speed = 100
        self.grounded = False
        self.dir = Player.RIGHT
        # controls
        self.moveleft = False
        self.moveright = False
        self.jump = False

    def input(self, keys: pygame.key.ScancodeWrapper):
        self.moveleft = keys[pygame.K_a]
        self.moveright = keys[pygame.K_d]
        self.jump = keys[pygame.K_w] or keys[pygame.K_SPACE]

    def update(self, platforms: list[Platform]):

        # move left and right
        if self.moveleft:
            self.physics.velocity.x = -self.run_speed
            self.current_anim = self.run_anim
            self.dir = Player.LEFT
        elif self.moveright:
            self.physics.velocity.x = self.run_speed
            self.current_anim = self.run_anim
            self.dir = Player.RIGHT
        else:
            self.current_anim = self.idle_anim
            self.physics.velocity.x = 0
        # jump
        if self.jump:
            self.physics.velocity.y -= self.jump_speed

        # physics
        self.physics.update()
        # collider
        for pf in platforms:
            self.physics.pos = self.collider.update_hard_collision(self.physics.pos, pf.collider)
        # update animation frame
        self.current_anim.update()

    def draw(self):
        if self.dir == Player.LEFT:
            globals.window.blit(pygame.transform.flip(self.current_anim.current_frame, True, False), self.collider.get_topleft().compat())
        else:
            globals.window.blit(self.current_anim.current_frame, self.collider.get_topleft().compat())
