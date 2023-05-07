"""
    Wrapper that handles UI elements such as:
    Buttons
    Text
    Switches
"""
import pygame
import globals as g
from UI.UI_element import UIElement, Text, Button, Switch
from vector import Vector

class UILayer:
    def __init__(self, *UI_elements: UIElement) -> None:
        for UI_i in UI_elements:
            if not isinstance(UI_i, UIElement):
                raise Exception("One or more of the arguments passed to UI_Layer is not a UI element")
        self.UI_elements = list(UI_elements)
        self.mouse_pos = pygame.mouse.get_pos()

    def input(self, pressed_keys):
        self.mouse_pos = pygame.mouse.get_pos()

    def update(self):
        for UI_i in self.UI_elements:
            if isinstance(UI_i, Button):
                mouse_in = UI_i.rect.collidepoint(self.mouse_pos)
                UI_i.mouse_enter = (not UI_i.selected) and mouse_in
                UI_i.mouse_leave = UI_i.selected and (not mouse_in)
            UI_i.update()

    def draw(self):
        for UI_i in self.UI_elements:
            UI_i.draw()
