"""
    Basic vector class with overloaded operators.
    as_tuple() returns a tuple like (x, y).
    from_tuple() creates a vector from a tuple like (x, y).
    Vectors can be either in screen resolution units or game space resolution units.
    The mode constructor argument can be Vector.SCREEN_RES or Vector.GAME_SPACE. By
    default it's Vector.GAME_SPACE, but it can be switched between the two using 
    to_game_space() or to_screen_res(). The compatible() method returns a tuple in
    Vector.SCREEN_RES
"""
from __future__ import annotations
import globals

class Vector:
    
    SCREEN_RES = 0
    GAME_SPACE = 1

    def __init__(self, x: int, y: int, mode: int=GAME_SPACE):
        self.x = x
        self.y = y
        self.mode = mode

    def as_tuple(self) -> tuple(int, int):
        return self.x, self.y
    
    # make compatible with pygame (convert to screen res mode and return as tuple)
    def compatible(self) -> tuple(int, int):
        match self.mode:
            case Vector.SCREEN_RES:
                return self.as_tuple()
            case Vector.GAME_SPACE:
                return self.to_screen_res().as_tuple()
        
    def to_game_space(self) -> Vector:
        if self.mode == Vector.SCREEN_RES:
            return Vector.from_tuple(((self * globals.game_space) / globals.screen_res).as_tuple())
        else:
            raise Exception("Vector is already in game space mode.")
    
    def to_screen_res(self):
        if self.mode == Vector.GAME_SPACE:
            return Vector.from_tuple(((self * globals.screen_res) / globals.game_space).as_tuple())
        else:
            raise Exception("Vector is already in screen resolution mode.")

    @classmethod
    def from_tuple(cls, tup, mode=GAME_SPACE) -> Vector:
        x, y = tup
        return cls(x, y, mode)
    
    # overloads
    def __add__(self, o) -> Vector:
        if isinstance(o, Vector):
            return Vector(self.x + o.x, self.y + o.y)
        elif isinstance(o, int):
            return Vector(self.x + o, self.y + o)
        
    def __sub__(self, o) -> Vector:
        if isinstance(o, Vector):
            return Vector(self.x - o.x, self.y - o.y)
        elif isinstance(o, int):
            return Vector(self.x - o, self.y - o)
        
    def __mul__(self, o) -> Vector:
        if isinstance(o, Vector):
            return Vector(self.x * o.x, self.y * o.y)
        elif isinstance(o, int):
            return Vector(self.x * o, self.y * o)
        
    def __truediv__(self, o) -> Vector:
        if isinstance(o, Vector):
            return Vector(round(self.x / o.x), round(self.y / o.y))
        elif isinstance(o, int):
            return Vector(round(self.x / o), round(self.y / o))
        
    def __floordiv__(self, o) -> Vector:
        if isinstance(o, Vector):
            return Vector(self.x // o.x, self.y // o.y)
        elif isinstance(o, int):
            return Vector(self.x // o, self.y // o)

    def __eq__(self, o) -> Vector:
        if isinstance(o, Vector):
            return self.x == o.x and self.y == o.y
