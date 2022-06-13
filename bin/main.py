import sys

from pygame import *

from bin.game import Game
from bin.settings import *

init()
font.init()

sc = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()

ses_path = ''
mode = 'game'


def game_func(session_path: str):
    global mode
    if mode != 'game':
        return False
    session = Game(session_path=session_path)
    while mode == 'game':
        mode = session.mode
        session.handle_events()
        session.update()
        sc.fill(color=WHITE)
        session.draw(sc=sc)
        display.update()
        clock.tick(FPS)
    return False


def main_menu_func():
    if mode != 'main_menu':
        return False
    for e in event.get():
        if e.type == QUIT:
            exit()
    return False


while mode != 'exit':
    game_func(session_path=ses_path)
    main_menu_func()
font.quit()
quit()
