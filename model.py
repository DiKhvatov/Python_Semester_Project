import pygame as pg
import numpy as np
import thorpy

from objects import *

def execution(delta, bullets, targets,  tanks, player_tank, screen):
    player_tank.move(delta)
    player_tank.draw(screen)
