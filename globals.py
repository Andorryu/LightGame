"""
    Global variables and constants.
    Contains:
    - running
    - fps
    - window and display info
    - game state
"""
import pygame
from vector import Vector
from states.main_menu import MainMenu
from states.game import Game
pygame.init()

win_info = pygame.display.Info() # get display info
screen_res = Vector(1600, 900, Vector.SCREEN_RES) # get display dimensions

# game space: resolution of the game's 2D space - the higher the better
game_space = Vector(3840, 2160)

# create window, running, and fps
window = pygame.display.set_mode(screen_res.as_tuple()) # make screen as big as screen resolution
running = True # must be set to True for game to run
fps = 60 # change this for default fps

# starting game state
game_state = Game()
