"""
    Program's entry point and location of outermost game loop.
"""
import pygame
import globals
import colors

class App:
    def __init__(self):
        pass

    def run(self):
        clock = pygame.time.Clock()
        while (globals.running):
            self.input()
            self.update()
            self.draw()
            clock.tick(globals.fps)

    def input(self):
        # close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                globals.running = False
        
        # collect key presses
        keys = pygame.key.get_pressed()
        globals.game_state.input(keys)

    def update(self):
        globals.game_state.update()
    
    def draw(self):
        globals.window.fill(colors.BLACK)
        globals.game_state.draw()
        pygame.display.flip()

if __name__ == '__main__':
    app = App()
    app.run()
