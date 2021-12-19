import pygame as pg
import numpy as np

from constants import *
from objects import *


def execution(delta, bullets, targets, tanks, player_tank):
    """
    Функция выполняет взаимодействие медлу объектами
    delta : float - разница по времени
    bullets : massive : class Bullet - массив с пулями
    targets : massive : class Target / Target_shooting - массив с целями
    tanks : massive : class Tank - массив с танками
    player_tank : class Tank - танк игрока
    """

    # проверяем выход за границы карты
    player_tank.wall_collision(delta)

    # передвижение танка игрока
    player_tank.move(delta)

    for bullet in bullets:
        # обработка событий с пулями
        # проверка выхода за границу
        bullet.wall_collision(world_left, world_right, world_up, world_down)

        # проверка создателя и столкновения с элемнтами
        if not bullet.parent == "tank":
            bullet.checking_breakthrough(tanks)
        if not bullet.parent == "target":
            bullet.checking_breakthrough(targets)
        if not bullet.parent == "player_tank":
            bullet.checking_breakthrough([player_tank])
        if not bullet.existion:
            bullets.remove(bullet)
            continue

        # передвижение пули
        bullet.move(delta)

    for target in targets:
        # проверка существования целей
        if not target.existion:
            fuckyou = pg.mixer.Sound("music/fuckyou.ogg")
            fuckyou.play()
            targets.remove(target)
            explosion = pg.mixer.Sound("music/zvuk-vzryva-dlya-video.ogg")
            explosion.play()
            continue

        # нацеливание на танк игрока
        target.aiming(player_tank)

        # стрельба стрелящей цели
        if target.type == "shooting target":
            bullet = target.shoot()
            target.charging(delta)
            if not bullet == 0:
                bullets.append(bullet)

        # проверка на столкновения танка с целью
        player_tank.target_collision(target)
        target.move(delta)

    for tank in tanks:
        if not tank.existion:
            tanks.remove(tank)
