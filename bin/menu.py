from pygame import *

from bin.button import Button


class Menu:
    def __init__(self):
        self.buttons = []

    def draw(self, sc):
        for btn in self.buttons:
            btn.draw(sc)

    def update(self, e):
        if e.type == MOUSEBUTTONDOWN:
            for btn in self.buttons:
                btn.is_pressed(e.pos)

    def add_button(self, _rect: tuple, text: str, callback):
        self.buttons.append(Button(_rect, text, callback))
