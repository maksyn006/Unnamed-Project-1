from random import randint
from pygame import *

from bin.settings import *
from bin.displaymode import *
init()

sc = display.set_mode((WIDTH, HEIGHT))
clock = time.Clock()


def game():
    if not display_mode['is_game']:
        return
    for e in event.get():
        if e.type == QUIT:
            set_display_mode_inactive('is_run')
    sc.fill(WHITE)
    draw.rect(sc, RED, (randint(0, WIDTH), randint(0, HEIGHT), 50, 50))
    display.update()
    clock.tick(FPS)


def main_menu():
    if not display_mode['is_main_menu']:
        return
    for e in event.get():
        if e.type == QUIT:
            set_display_mode_inactive('is_run')
        if e.type == MOUSEBUTTONDOWN:
            if 0 < e.pos[0] < 200 and 0 < e.pos[1] < 200:
                set_display_mode_inactive('is_run')
    sc.fill(WHITE)
    draw.rect(sc, GREEN, (randint(0, WIDTH), randint(0, HEIGHT), 50, 50))
    display.update()
    clock.tick(FPS)


while display_mode['is_run']:
    game()
    main_menu()
quit()
