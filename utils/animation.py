"""
    Animation takes a list of surface objects (preferably loaded from Spritesheet class)
"""

import pygame

class Animation:
    def __init__(self, frames: list[pygame.Surface], duration: int) -> None:
        """
            duration: how long in (milliseconds) should the animation last from start to finish?
            Each frame will last an equal amount of time.
        """
        self.frames = frames
        self.duration = duration
        self.num_frames = len(self.frames)
        self.frame_duration = self.duration/self.num_frames
        self.current_frame = self.frames[0]
        self.clock = pygame.time.Clock()
        self.runtime = 0

    def update(self):
        self.runtime += self.clock.tick()
        self.runtime %= self.duration
        for i in range(self.num_frames):
            if self.runtime < (i + 1)*self.frame_duration:
                self.current_frame = self.frames[i]
                break
        
