import pygame as pg
import numpy as np


from random import randint

from constants import *
from objects import *
from visual import *
from model import *
from server import *
from client import *


screen = pg.display.set_mode((window_width, window_height))


def client_init():
    cl = Client()
    cl.enter_menu(screen)


def server_init():
    serv = Server()
    serv.enter_port(screen)
    serv.bind()


def main():
    """
    Главная функция игры, на которой завязано все взаимодействие, отрисовка и перемещения
    """

    """
    Инициализация  переменных для дальнейшего использования

    timer : None - таймер с временем

    alive : bool - флаг неоконченной игры

    bullets : massive - массив для записывания туда пуль

    targets : massive - массив для записывания туда целей

    tanks : massive - массив для записывания туда танков

    player_tank : class Tank - танк игрока
    """

    timer = None
    alive = True
    bullets = []
    targets = []
    tanks = []
    player_tank = Tank()

    # словарь с клавишами и их флагами
    FLAGS = {
        "K_w": False,
        "K_a": False,
        "K_s": False,
        "K_d": False,
        "K_SPACE": False,
        "counter": 0,
    }

    def handle_events(events, player_tank, alive):
        """
        Функция обработчик событий с клавиатуры и мыши

        events : massive : pygame.event - массив с событиями

        player_tank : class Tank - танк игрока для изменения его параметров

        alive : bool -  флаг продолжения игры
        """

        # пересчет фпс для зарядки танка игрока
        max_count = 50 * FPS / 120

        # обработка событий
        for event in events:
            # выяснение выполненного события
            if event.type == pg.QUIT:
                alive = False
            else:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        FLAGS.update({"K_w": True})
                    if event.key == pg.K_s:
                        FLAGS.update({"K_s": True})
                    if event.key == pg.K_d:
                        FLAGS.update({"K_d": True})
                    if event.key == pg.K_a:
                        FLAGS.update({"K_a": True})
                    if event.key == pg.K_SPACE:
                        FLAGS.update({"K_SPACE": True})

                if event.type == pg.KEYUP:
                    if event.key == pg.K_w:
                        FLAGS.update({"K_w": False})
                    if event.key == pg.K_s:
                        FLAGS.update({"K_s": False})
                    if event.key == pg.K_a:
                        FLAGS.update({"K_a": False})
                    if event.key == pg.K_d:
                        FLAGS.update({"K_d": False})
                    if event.key == pg.K_SPACE:
                        FLAGS.update({"K_SPACE": False})

        # изменение скорости танка
        if FLAGS.get("K_w") or FLAGS.get("K_s"):
            if FLAGS.get("K_w"):
                # player_tank.v = v_tank
                player_tank.a = 0.3
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

        # стрельба танка
        if FLAGS.get("K_SPACE") and FLAGS.get("counter") > max_count:
            FLAGS.update({"counter": 0})
            slap = pg.mixer.Sound("music/slap7.ogg")
            slap.play()
            bullets.append(
                Bullet(
                    player_tank.x + 6 / 5 * player_tank.r * np.cos(player_tank.angle),
                    player_tank.y + 6 / 5 * player_tank.r * np.sin(player_tank.angle),
                    player_tank.angle,
                    v_bullet + player_tank.v,
                    "player_tank",
                )
            )

        FLAGS.update({"counter": FLAGS.get("counter") + 1})

        return alive

    clock = pg.time.Clock()
    pg.init()
    screen = pg.display.set_mode((window_width, window_height))

    # загрузка картинок для фона
    IMAGES = []
    for i in range(100):
        IMAGES.append(pg.image.load("fractals/" + str(i) + ".png").convert_alpha())

    # Загрузка внутриигровой музыки
    slap = pg.mixer.Sound("music/slap7.ogg")
    # pg.mixer.music.load("music/evgeny-kissin-prokofiev-piano-concerto-no-3-in-c-op-26-1-andante-alleg.ogg")
    pg.mixer.music.load(
        "music/Chicago-Symphony-Orchestra_-Sir-Georg-Solti-—-Prokofiev-Romeo-and-Juliet_-Op.-64-_-Act-1-13.ogg"
    )
    pg.mixer.music.play(-1, 0.0)

    for round_number in range(10):
        """
        Цикл с раундами
        """
        if not alive:
            break

        player_tank.new_round()

        bullets.clear()
        tanks.clear()
        targets.clear()

        for i in range(100 * round_number):
            """
            Создание обычных и стреляющих целей
            """
            targets.append(
                Target(
                    randint(world_left, world_right),
                    randint(world_up, world_down),
                    randint(0, 5),
                )
            )
            targets.append(
                Target_shooting(
                    randint(world_left, world_right),
                    randint(world_up, world_down),
                    randint(0, 5),
                )
            )

        drawer = Drawer(screen)

        # tanks.append(Tank())

        delta = 0.1 * FPS / 12

        while alive:

            execution(delta, bullets, targets, tanks, player_tank)
            alive = handle_events(pg.event.get(), player_tank, alive)
            drawer.update(player_tank, bullets, targets, tanks, screen, delta, IMAGES)
            if len(targets) == 0:
                break

            clock.tick(FPS)


pg.init()
pg.mixer.init()

# nickname = new_game(screen)
"""
choice = join_create(screen)

if choice == "e":
    quit()
elif choice == "s":
    serv = Server(nickname)
    serv.enter_port(screen)
    serv.bind()
elif choice == "c":
    cl = Client(nickname)
    cl.enter_menu(screen)
"""
main()
