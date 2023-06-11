"""
    Global variables and constants.
    Contains:
    - running
    - fps
    - window and display info
    - game state
"""
import pygame
from utils.vector import Vector
from states.main_menu import MainMenu
from states.game import Game
pygame.init()

# for the frame that condition is true, bool becomes true. Every frame after, it is false
def edge_trigger(condition: bool, trigger: bool):
    if trigger:
        trigger = False
    if condition:
        trigger = True
    return trigger

win_info = pygame.display.Info() # get display info
screen_res = Vector(1200, 675, Vector.SCREEN_RES) # get display dimensions

# game space: resolution of the game's 2D space - the higher the better
game_space = Vector(16000, 9000)

# create window, running, and fps
window = pygame.display.set_mode(screen_res.as_tuple()) # make screen as big as screen resolution
running = True # must be set to True for game to run
fps = 60 # change this for default fps

# starting game state
game_state = Game()
