import pygame as pg
import numpy as np

from random import randint

from constants import *
from objects import *
from visual import *
from model import *

global world_left
global world_right
global world_up
global world_down



global window_height
global window_width

global delta
global v_tank
global w_tank
global v_bullet
global FPS

timer = None
alive = True
bullets = []
targets = []
tanks = []
screen = pg.display.set_mode((window_width, window_height))
player_tank = Tank()

print("We are fucked1")

FLAGS = {
            'K_w' : False,
            'K_a' : False,
            'K_s' : False,
            'K_d' : False,
            'K_SPACE' : False,
            'counter' : 0,
        }


def handle_events(events, player_tank, alive):
    global w0
    global v0
    global v_bullet
    global bullets
    global FLAGS
    global FPS

    max_count = 10 * FPS / 120

    for event in events:
        if event.type == pg.QUIT:
            alive = False
        else:
            if event.type == pg.KEYDOWN:
                # TODO: пофиксить попеременное переключение клавиш
                if event.key == pg.K_w:
                    FLAGS.update({"K_w":True})
                if event.key == pg.K_s:
                    FLAGS.update({"K_s":True})
                if event.key == pg.K_d:
                    FLAGS.update({"K_d":True})
                if event.key == pg.K_a:
                    FLAGS.update({"K_a":True})
                if event.key == pg.K_SPACE:
                    FLAGS.update({"K_SPACE":True})

            if event.type == pg.KEYUP:
                if event.key == pg.K_w:
                    FLAGS.update({"K_w" : False})
                if event.key == pg.K_s:
                    FLAGS.update({"K_s" : False})
                if event.key == pg.K_a:
                    FLAGS.update({"K_a" : False})
                if event.key == pg.K_d:
                    FLAGS.update({"K_d" : False})
                if event.key == pg.K_SPACE:
                    FLAGS.update({"K_SPACE":False})

    if FLAGS.get("K_w") or FLAGS.get("K_s"):
        if FLAGS.get("K_w"):
            player_tank.v = v_tank
        if FLAGS.get("K_s"):
            player_tank.v = -v_tank
        if FLAGS.get("K_w") and FLAGS.get("K_s"):
            player_tank.v = 0
    else:
        player_tank.v = 0

    if FLAGS.get("K_a") or FLAGS.get("K_d"):
        if FLAGS.get("K_a"):
            player_tank.w = -w_tank
        if FLAGS.get("K_d"):
            player_tank.w = w_tank
        if FLAGS.get("K_a") and FLAGS.get("K_d"):
            player_tank.w = 0
    else:
        player_tank.w = 0

    if FLAGS.get("K_SPACE") and FLAGS.get("counter") > max_count:
        FLAGS.update({"counter" : 0})
        bullets.append(Bullet(player_tank.x + 6/5 * player_tank.r * np.cos(player_tank.angle) , player_tank.y +
            6/5 * player_tank.r * np.sin(player_tank.angle), player_tank.angle, v_bullet + player_tank.v, "player_tank"))

    FLAGS.update({"counter" : FLAGS.get("counter") + 1})

    return alive


def main():
    global alive
    global delta
    global timer
    global bullets
    global targets
    global tanks
    global player_tank
    global FPS

    global world_left
    global world_right
    global world_up
    global world_down

    global window_height
    global window_width

    clock = pygame.time.Clock()

    for round_number in range(10):

        print(round_number)

        player_tank.x = 0
        player_tank.y = 0
        player_tank.v = 0

        bullets.clear()
        tanks.clear()
        targets.clear()

        for i in range(round_number):
            targets.append(Target(randint(world_left, world_right), randint(world_up, world_down), randint(0, 5)))
            targets.append(Target_shooting(randint(world_left, world_right), randint(world_up, world_down), randint(0, 5)))


        drawer = Drawer(screen)

        tanks.append(Tank())
        #print(type(Target_shooting()))

        delta = 0.1 * FPS / 12
        while alive:

            execution(delta, bullets, targets,  tanks, player_tank)
            alive = handle_events(pg.event.get(), player_tank, alive)
            drawer.update(player_tank, bullets, targets, tanks, screen)
            if len(targets) == 0:
                break

            clock.tick(FPS)

print("We are fucked")

pg.init()

nickname = new_game(screen)


main()
