
from __future__ import annotations
from utils.vector import Vector
import math

class Line:
    HORIZONTAL = 0
    VERTICAL = 1
    def __init__(self, p1: Vector, p2: Vector) -> None:
        self.p1 = p1
        self.p2 = p2
        self.slope = self.get_slope()
        self.y_intercept = self.get_y_intercept()
    
    def intersect(self, other: Line) -> tuple[Vector, int]:
        """
            find the point at which the two lines intersect and give the direction
        """

        if self.slope == other.slope:
            return None, None
        elif self.slope == math.inf:
            dir = Line.HORIZONTAL
            x = self.p1.x
            y = other.slope*x + other.y_intercept
        elif other.slope == math.inf:
            dir = Line.VERTICAL
            x = self.p1.x
            y = self.slope*x + self.y_intercept
        else:
            dir = Line.HORIZONTAL
            x = (other.y_intercept - self.y_intercept)/(self.slope - other.slope)
            y = (other.slope*self.y_intercept - self.slope*other.y_intercept)/(other.slope - self.slope)
        return Vector(x, y), dir

    def get_slope(self):
        try:
            return (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x)
        except ZeroDivisionError:
            return math.inf

    def get_y_intercept(self):
        return self.p1.y - self.slope*self.p1.x

class Collider:
    def __init__(self, pos: Vector, size: Vector) -> None:
        self.pos = pos # may remove this later
        self.size = size

    def get_sides(self) -> tuple[int, int, int, int]:
        """
            -> (top, right, bottom, left)
        """
        halfx, halfy = self.size.x/2, self.size.y/2
        return self.pos.y - halfy, self.pos.x + halfx, self.pos.y + halfy, self.pos.x - halfx

    def test_collision(self, other: Collider) -> bool:
        s_top, s_right, s_bottom, s_left = self.get_sides()
        o_top, o_right, o_bottom, o_left = other.get_sides()
        result = False
        if s_top < o_bottom and s_bottom > o_top and s_right > o_left and s_left < o_right:
            result = True
        return result
    
    def get_topleft(self):
        sides = self.get_sides()
        return Vector(sides[3], sides[0])

    def update_hard_collision(self, pos: Vector, other: Collider) -> Vector:
        """
            Use this instead of update or test_collision to sync position and stop the object if it collides.
        """
        lastpos = self.pos        
        self.pos = pos

        if self.test_collision(other):
            # get points for drawing lines
            topleft = other.pos - other.size/2 - self.size/2
            topright = Vector(
                other.pos.x + other.size.x/2 + self.size.x/2,
                other.pos.y - other.size.y/2 - self.size.y/2
            )
            bottomright = other.pos + other.size/2 + self.size/2
            bottomleft = Vector(
                other.pos.x - other.size.x/2 - self.size.x/2,
                other.pos.y + other.size.y/2 + self.size.y/2
            )
            # draw lines to connect points
            top_line = Line(
                topleft,
                topright
            )
            right_line = Line(
                topright,
                bottomright
            )
            bottom_line = Line(
                bottomright,
                bottomleft
            )
            left_line = Line(
                bottomleft,
                topleft
            )
            collideline = Line(
                lastpos,
                self.pos
            )
            for line in top_line, right_line, bottom_line, left_line:
                collision_point, dir = collideline.intersect(line)
                if collision_point == None:
                    continue

                if collision_point.x <= max(self.pos.x, lastpos.x) and collision_point.x >= min(self.pos.x, lastpos.x):
                    if collision_point.y <= max(self.pos.y, lastpos.y) and collision_point.y >= min(self.pos.y, lastpos.y):
                        if dir == Line.HORIZONTAL:
                            self.pos.y = round(collision_point.y)
                        else:
                            self.pos.x = round(collision_point.x)
                        break
        return self.pos
