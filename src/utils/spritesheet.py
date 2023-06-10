"""
    Class to handle spritesheets (since pygame doesn't have a built in spritesheet class)
    Spritesheets should not have margins or paddings, each image should be right next to each other
"""

import pygame
from utils.vector import Vector

class Spritesheet:
    def __init__(self, img_path) -> None:
        self.img = pygame.image.load(img_path)

    def slice(self, dim: Vector, size: Vector=Vector(0, 0)) -> list[pygame.Surface]:
        """
            dim: dimensions in # of cells - reads by row, left to right
            size: size for each image
        """
        sprites: list[pygame.Surface] = []
        sheet_size = self.img.get_size()
        cell_w, cell_h = sheet_size[0]/dim.x, sheet_size[1]/dim.y
        for y in range(dim.y):
            for x in range(dim.x):
                rect = pygame.Rect((x*cell_w, y*cell_h, cell_w, cell_h))
                sprite = pygame.Surface(rect.size)
                sprite.blit(self.img, (0, 0), rect)
                if size.x != 0 and size.y != 0:
                    sprite = pygame.transform.scale(sprite, size.compat())
                sprites.append(sprite)
        return sprites
