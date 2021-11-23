import pygame as pg
import numpy as np
import thorpy

from constants import *
from objects import *
from visual import *
from model import *

timer = None
alive = True
bullets = []
targets = []
tanks = []
player_tank = Tank()

global world_left
global world_right
global world_up
global world_down

global delta
global v_tank
global w_tank
global v_bullet

keys_flags = [False] * 4


def handle_events(events, menu, player_tank, alive):
    global w0
    global v0
    global v_bullet
    global bullets
    for event in events:
        menu.react(event)
        if event.type == pg.QUIT:
            alive = False
        else:
            if event.type == pg.KEYDOWN:
                # TODO: пофиксить попеременное переключение клавиш
                if event.key == pg.K_w:
                    player_tank.v = v_tank
                if event.key == pg.K_s:
                    player_tank.v = -v_tank
                if event.key == pg.K_d:
                    player_tank.w = w_tank
                if event.key == pg.K_a:
                    player_tank.w = -w_tank
                if event.key == pg.K_SPACE:
                    # TODO: зажатый пробел
                    bullets.append(Bullet(player_tank.x, player_tank.y, player_tank.angle, v_bullet))
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
        execution(delta, bullets, targets,  tanks, player_tank)
        drawer.update(player_tank, bullets, targets, tanks, box)




main()
