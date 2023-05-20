"""
    interface for all playable levels
"""
import pygame
from states.state import State
from player import Player
import globals
from utils.vector import Vector
import utils.colors as colors
from game_platform import Platform
from entity import Entity



class Game(State):
    def __init__(self) -> None:
        self.player = Player()
        self.platforms: list[Platform] = [
            Platform()
        ]

    def input(self, keys):
        self.player.input(keys)

    def update(self):
        self.check_player_platform_collision()
        self.player.update()

    def draw(self):
        self.player.draw()
        for platform in self.platforms:
            platform.draw()

    def check_player_platform_collision(self):
        # grounded
        self.player.grounded = False
        for platform in self.platforms:
            if platform.rect.clipline(self.player.ray.compat()):
                self.player.grounded = True
        # every other collision
        for platform in self.platforms:
            if platform.rect.colliderect(self.player.rect):
                match self.check_collision_direction(platform, self.player):
                    case "top":
                        pass
                    case "right":
                        pass
                    case "bottom":
                        pass
                    case "left":
                        pass

    # which side of rect1 is rect2 on?
    def check_collision_direction(self, rect1: pygame.Rect, rect2: pygame.Rect):
        top, right, bottom, left = abs(rect2.bottom - rect1.top), abs(rect2.left - rect1.right), abs(rect2.top - rect1.bottom), abs(rect2.right - rect1.left)
        smallest = min(top, right, bottom, left)
        if smallest == top:
            return "top"
        elif smallest == right:
            return "right"
        elif smallest == bottom:
            return "bottom"
        else:
            return "left"
