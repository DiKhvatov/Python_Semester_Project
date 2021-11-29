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

    player_tank.wall_collision(delta)
    #print(player_tank.health)
    player_tank.move(delta)

    for bullet in bullets:
        bullet.wall_collision(world_left, world_right, world_up, world_down)
        if not bullet.parent == "tank":
            bullet.checking_breakthrough(tanks)
        if not bullet.parent == "target":
            bullet.checking_breakthrough(targets)
        if not bullet.parent == "player_tank":
            bullet.checking_breakthrough([player_tank])
        if not bullet.existion:
            bullets.remove(bullet)
            continue
        bullet.move(delta)

    for target in targets:
        if not target.existion:
            targets.remove(target)
            continue
        target.aiming(player_tank)
        if target.type == "shooting target":
            bullet = target.shoot()
            target.charging(delta)
            if not bullet == 0:
                bullets.append(bullet)
        target.move(delta)

    for tank in tanks:
        if not tank.existion:
            tanks.remove(tank)
