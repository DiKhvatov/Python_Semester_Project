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
v0 = 5
w0 = 0.1


def handle_events(events, menu, player_tank, alive):
    global w0
    global v0
    for event in events:
        menu.react(event)
        if event.type == pg.QUIT:
            alive = False
        else:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    player_tank.v = v0
                if event.key == pg.K_s:
                    player_tank.v = -v0
                if event.key == pg.K_d:
                    player_tank.w = w0
                if event.key == pg.K_a:
                    player_tank.w = -w0
            if event.type == pg.KEYUP:
                if event.key == pg.K_w or event.key == pg.K_s:
                    player_tank.v = 0
                if event.key == pg.K_d or event.key == pg.K_a:
                    player_tank.w = 0
    return alive


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



        alive = handle_events(pg.event.get(), menu, player_tank, alive)

        surface = execution(delta, bullets, targets,  tanks, player_tank)
        #pg.draw.circle(drawer.screen, (0,255,255), (50, 50), 10)
        drawer.update([player_tank], box)




main()
