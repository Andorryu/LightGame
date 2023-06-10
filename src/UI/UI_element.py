"""
    UI elements live here:
    Text
    Button
    Switch
"""
import pygame
import utils.colors as colors
import globals
from utils.vector import Vector

def to_screen_res_y(num: int):
    return round((num * globals.screen_res.y) / globals.game_space.y)

class UIElement:
    # position flags
    TOPLEFT = 0
    CENTER = 1
    TOPRIGHT = 2
    BOTTOMLEFT = 3
    BOTTOMRIGHT = 4
    CENTERLEFT = 5
    CENTERTOP = 6
    CENTERRIGHT = 7
    CENTERBOTTOM = 8
    def __init__(self) -> None:
        """Initialize UI element"""
        self.surf: pygame.surface.Surface = None
        self.rect: pygame.rect.Rect = None

    def update(self) -> None:
        """Update UI element"""
        pass

    def draw(self) -> None:
        """Update UI element"""
        pass

    def create_rect(self, pos_mode: int, pos: Vector):
        # position based on pos_mode
        match pos_mode:
            case UIElement.TOPLEFT:
                self.rect = self.surf.get_rect(topleft=pos.compat())
            case UIElement.CENTER:
                self.rect = self.surf.get_rect(center=pos.compat())
            case UIElement.TOPRIGHT:
                self.rect = self.surf.get_rect(topright=pos.compat())
            case UIElement.BOTTOMLEFT:
                self.rect = self.surf.get_rect(bottomleft=pos.compat())
            case UIElement.BOTTOMRIGHT:
                self.rect = self.surf.get_rect(bottomright=pos.compat())
            case UIElement.CENTERLEFT:
                self.rect = self.surf.get_rect(midleft=pos.compat())
            case UIElement.CENTERTOP:
                self.rect = self.surf.get_rect(midtop=pos.compat())
            case UIElement.CENTERRIGHT:
                self.rect = self.surf.get_rect(midright=pos.compat())
            case UIElement.CENTERBOTTOM:
                self.rect = self.surf.get_rect(midbottom=pos.compat())

class Text(UIElement):
    def __init__(
        self,
        text: str="Example Text",
        font_path: str=None,
        size: int=100,
        color: tuple[int, int, int]=colors.WHITE,
        pos: Vector= Vector(0, 0),
        pos_mode: int=UIElement.CENTER,
        just_font: bool=False # if true, only specify font_path and size
    ) -> None:
        size = to_screen_res_y(size) # assume size was given in game space res and translate to screen res

        self.font = pygame.font.Font(font_path, size)
        if not just_font:
            self.create_surf(text, color)
            self.create_rect(pos_mode, pos)

    def create_surf(self, text, color):
        self.surf = self.font.render(text, True, color)

    def update(self):
        pass

    def draw(self):
        globals.window.blit(self.surf, self.rect)

class Button(UIElement):
    def __init__(
        self,
        text: str="Example Text",
        font_path: str=None,
        font_size: int=100,
        text_color: tuple[int, int, int]=colors.BLACK,
        pos: Vector= Vector(0, 0),
        pos_mode: int=UIElement.CENTER,
        bg_color: tuple[int, int, int]=colors.WHITE,
        text_color_sel: tuple[int, int, int]=colors.DARK_GRAY,
        bg_color_sel: tuple[int, int, int]=colors.CYAN,
        margins: int=50
    ) -> None:
        self.text = Text(
            font_path=font_path,
            size=font_size,
            just_font=True
        )
        # calculate size
        expected_font_size: Vector = Vector.from_tuple(self.text.font.size(text))
        size = expected_font_size + margins*2
        # set surf and rect of background
        self.surf = pygame.surface.Surface(size.as_tuple())
        self.create_rect(pos_mode, pos)
        self.surf.fill(bg_color)
        self.pos = pos
        # make text
        self.text.create_surf(text, text_color)
        self.text.create_rect(UIElement.CENTER, Vector.from_tuple(self.rect.center, Vector.SCREEN_RES))
        self.raw_text = text
        # set color attributes
        self.text_color = text_color
        self.text_color_sel = text_color_sel
        self.bg_color = bg_color
        self.bg_color_sel = bg_color_sel
        # selected
        self.selected = False
        self.mouse_enter = False # only True on the one frame when mouse enters button
        self.mouse_leave = False # like mouse_enter but when mouse leaves

    def update(self) -> None:
        if self.mouse_enter:
            self.selected = True
            self.text.create_surf(self.raw_text, self.text_color_sel)
            self.surf.fill(self.bg_color_sel)
        elif self.mouse_leave:
            self.selected = False
            self.text.create_surf(self.raw_text, self.text_color)
            self.surf.fill(self.bg_color)

    def draw(self) -> None:
        globals.window.blit(self.surf, self.rect)
        self.text.draw()

    def action(self) -> None:
        pass # override this function in the game state that the button exists

class Switch(UIElement):
    def __init__(self) -> None:
        pass