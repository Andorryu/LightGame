"""
    interface for all playable levels
"""
import pygame
from states.state import State
from player import Player

class Game(State):
    def __init__(self) -> None:
        self.player = Player()

    def input(self, keys):
        self.player.input(keys)

    def update(self):
        self.player.update()

    def draw(self):
        self.player.draw()
