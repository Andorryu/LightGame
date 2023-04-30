"""
    Program's entry point and location of outermost game loop.
"""
import pygame
pygame.init()
import globals as g

class Game:
    def __init__(self):
        self.keys = pygame.key.get_pressed()

    def run(self):
        clock = pygame.time.Clock()
        while (g.running):
            self.input()
            self.update()
            self.draw()
            clock.tick(g.fps)

    def input(self):
        # close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g.running = False
        
        # collect key presses
        self.keys = pygame.key.get_pressed()

    def update(self):
        pass
    
    def draw(self):
        pass

if __name__ == '__main__':
    game = Game()
    game.run()
