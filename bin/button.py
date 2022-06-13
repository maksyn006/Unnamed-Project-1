from pygame import font


class Button:
    def __init__(self, _rect: tuple, text: str, callback):
        self.x, self.y, self.w, self.h = _rect
        self.text = text
        self.callback = callback

    def pressed(self):
        self.callback()

    def is_pressed(self, pos):
        if self.x < pos[0] < self.x + self.w and self.y < pos[1] < self.y + self.h:
            self.pressed()

    def draw(self, sc, font_size=30):
        font_d = font.SysFont('arial', font_size)
        text_surface = font_d.render(self.text, True, (0, 0, 0))
        sc.blit(text_surface, self.pos)

    @property
    def rect(self):
        return self.x, self.y, self.w, self.h

    @property
    def pos(self):
        return self.x, self.y
