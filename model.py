import pygame as pg
import numpy as np
import thorpy

from constants import *
from objects import *

def execution(delta, bullets, targets,  tanks, player_tank):
    global world_left
    global world_right
    global world_up
    global world_down

    player_tank.move(delta)

    for bullet in bullets:
        bullet.wall_collision(world_left, world_right, world_up, world_down)
        bullet.checking_breakthrough(tanks)
        bullet.checking_breakthrough(targets)
        #bullet.checking_breakthrough([player_tank])
        if not bullet.existion:
            bullets.remove(bullet)
            continue
        bullet.move(delta)
