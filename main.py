import pygame as pg
import numpy as np
import thorpy

from objects import *
from visual import *
from model import *

timer = None
alive = True
bullets = []
targets = []
tanks = []
player_tank = Tank()
delta = 0.1

def main():
    global alive
    global delta
    global timer
    global bullets
    global targets
    global tanks
    global player_tank

    pg.init()
    window_height = 1000
    window_width = 1000
    screen = pg.display.set_mode((window_width, window_height))

    drawer = Drawer(screen)
    menu, box, rounds, score = init_ui(screen)

    while alive:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                alive = False

        handle_events(pg.event.get(), menu)

        execution(delta, bullets, targets,  tanks, player_tank, screen)

        drawer.update([], box)


main()
