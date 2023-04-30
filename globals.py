"""
    Global variables and constants.
    Contains:
    - running
    - fps
    - game state
"""
import pygame

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, tup):
        x, y = tup
        return cls(x, y)
    
    def __add__(self, o):
        if isinstance(o, Vector):
            return self.x + o.x, self.y + o.y
        elif isinstance(o, int):
            return self.x + o, self.y + o
        
    def __mul__(self, o):
        if isinstance(o, Vector):
            return self.x * o.x, self.y * o.y
        elif isinstance(o, int):
            return self.x * o, self.y * o
        
    def __truediv__(self, o):
        if isinstance(o, Vector):
            return round(self.x / o.x), round(self.y / o.y)
        elif isinstance(o, int):
            return round(self.x / o), round(self.y / o)
        
    def __floordiv__(self, o):
        if isinstance(o, Vector):
            return self.x // o.x, self.y // o.y
        elif isinstance(o, int):
            return self.x // o, self.y // o

    def __eq__(self, o):
        if isinstance(o, Vector):
            return self.x == o.x and self.y == o.y

running = True
fps = 60

win_info = pygame.display.Info()
screen_res = (win_info.current_w, win_info.current_h)
window = pygame.display.set_mode(screen_res)


