
from utils.vector import Vector

class Physics:
    def __init__(self, pos: Vector, velocity: Vector=Vector(0, 0), acceleration: Vector=Vector(0, 0)) -> None:
        self.pos = pos
        self.velocity = velocity
        self.acceleration = acceleration

    def update(self):
        self.velocity += self.acceleration
        self.pos += self.velocity
