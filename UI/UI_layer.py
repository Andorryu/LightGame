"""
    Wrapper that handles UI elements such as:
    Buttons
    Text
    Switches
"""
import pygame
import globals as g
from UI.UI_element import UIElement, Text, Button, Switch
from utils.vector import Vector

class UILayer:
    def __init__(self, *UI_elements: UIElement) -> None:
        for UI_i in UI_elements:
            if not isinstance(UI_i, UIElement):
                raise Exception("One or more of the arguments passed to UI_Layer is not a UI element")
        self.UI_elements = list(UI_elements)
        self.mouse_pos = pygame.mouse.get_pos()

    def input(self, keys):
        self.mouse_pos = pygame.mouse.get_pos()
        self.left, self.middle, self.right = pygame.mouse.get_pressed()

    def update(self):
        for UI_i in self.UI_elements:
            if isinstance(UI_i, Button):
                self.select_button(UI_i)
                if UI_i.selected and self.left:
                    UI_i.action()
            UI_i.update()
    
    def select_button(self, button: Button):
        mouse_in = button.rect.collidepoint(self.mouse_pos)
        button.mouse_enter = (not button.selected) and mouse_in
        button.mouse_leave = button.selected and (not mouse_in)

    def draw(self):
        for UI_i in self.UI_elements:
            UI_i.draw()
