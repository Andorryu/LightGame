"""

"""
from UI.UI_layer import UILayer
from UI.UI_element import UIElement, Text, Button, Switch
from vector import Vector
from states.game import Game
import globals
import colors

def goto_game():
    globals.game_state = Game()

class MainMenu:
    def __init__(self) -> None:
        self.UI_layer = UILayer(
            Text(
                text="Welcome to the Game!",
                size=200,
                pos=globals.screen_res.to_game_space()/2 - Vector(0, 800)
            ),
            Button(
                text="Hello!",
                font_size=200,
                pos=globals.screen_res.to_game_space()/2,
                text_color_sel=colors.DARK_GRAY,
                bg_color_sel=colors.LIGHT_GRAY
            )
        )

    def input(self, pressed_keys):
        self.UI_layer.input(pressed_keys)

    def update(self):
        self.UI_layer.update()

    def draw(self):
        self.UI_layer.draw()
