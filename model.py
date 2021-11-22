import pygame as pg
import numpy as np
import thorpy

from objects import *

def execution(delta, bullets, targets,  tanks, player_tank):
    player_tank.move(delta)
