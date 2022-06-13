from pygame import *


class Game:
    def __init__(self, session_path: str):
        self.mode = 'game'

    def update(self):
        pass

    def draw(self, sc):
        pass

    def handle_events(self):
        for e in event.get():
            if e.type == QUIT:
                self.mode = 'exit'

