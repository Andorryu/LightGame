"""
    interface for all playable levels
"""

from state import State

class Game(State):
    def __init__(self) -> None:
        super().__init__()
        
