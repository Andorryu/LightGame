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
        self.player.update()

    def draw(self):
        self.player.draw()
        for platform in self.platforms:
            platform.draw()
