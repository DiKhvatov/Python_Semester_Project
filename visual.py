import pygame as pg

from constants import *

"""
Есть идея засунуть все связанное с рисованием в этот файл
"""


class Drawer:
    """
    Стыренный класс из проекта солнечной системы для отрисовки
    """

    def __init__(self, screen):
        """
        Инициализация
        screen : pygame.surface - экран для отрисовки
        counter : float - счетчик для отрисовки фона
        direction : float - значения 0,1 для зацикливания картинки
        """
        self.screen = screen
        self.counter = 0
        self.direction = 1

    def update(self, player_tank, bullets, targets, tanks, screen, delta, IMAGES):
        """
        player_tank : class Tank - танк игрока
        bullets : massive  - массив с пулями для отрисовки
        targets : massive - массив с целями для отрисовки
        tanks : massive - танки для отрисовки
        screen : pygame.surface - экран для отрисовки
        delta : float - промежуток времени
        IMAGES : massive - массив с картинками для отрисовки изменяющегося фрактала
        Предполагается, что каждая имеет функцию отрисовки draw c одинаковыми входными параметрами
        """
        global window_height
        global window_width

        self.screen.fill((0, 0, 0))

        rect_x = world_left - player_tank.x + window_width / 2
        rect_y = world_up - player_tank.y + window_height / 2
        rect_width = world_right - world_left
        rect_height = world_down - world_up

        pg.draw.rect(
            self.screen, (255, 255, 255), (rect_x, rect_y, rect_width, rect_height)
        )

        pg.Surface.blit(self.screen, IMAGES[int(self.counter)], (rect_x, rect_y))
        if self.direction == 1:
            self.counter += delta * 0.3
        else:
            self.counter -= delta * 0.3

        if self.counter >= 99:
            self.direction = 0

        if self.counter <= 0:
            self.direction = 1
        # pygame.Surface.blit(self.screen, fractal_surface, (0,0))

        player_tank.draw(
            self.screen,
            player_tank.x - window_width / 2,
            player_tank.y - window_width / 2,
            screen,
        )

        for tank in tanks:
            tank.draw(
                self.screen,
                player_tank.x - window_width / 2,
                player_tank.y - window_width / 2,
                screen,
            )

        for bullet in bullets:
            bullet.draw(
                self.screen,
                player_tank.x - window_width / 2,
                player_tank.y - window_width / 2,
            )

        for target in targets:
            target.draw(
                self.screen,
                player_tank.x - window_width / 2,
                player_tank.y - window_width / 2,
                screen,
            )

        pg.display.update()


def new_game(screen):
    """
    Функцию писал Дмитрий, видимо это окно с вводом имени
    screen : pygame.surface - экран
    """
    font = pg.font.SysFont("Helvetica Neue", 50)
    font_medium = pg.font.SysFont("Helvetica Neue", 40)

    init = True
    Name = ""
    WIDTH = window_width
    HEIGHT = window_height
    while init:
        screen.fill((255, 255, 255))
        text_1 = font.render("Enter your name", False, (0, 0, 0))
        text_2 = font.render("Submit", False, (0, 0, 0))
        text_name = font_medium.render(Name, False, (0, 0, 0))
        pg.draw.rect(
            screen,
            (0, 0, 0),
            (
                int(WIDTH / 2 - 3 - text_2.get_width() / 2),
                480 - 3,
                text_2.get_width() + 6,
                text_2.get_height() + 6,
            ),
            2,
        )
        screen.blit(text_1, (int(WIDTH / 2 - text_1.get_width() / 2), 270))
        screen.blit(text_2, (int(WIDTH / 2 - text_2.get_width() / 2), 480))
        pg.draw.rect(screen, ((0, 0, 0)), (WIDTH / 2 - 170, 390, 340, 50), 2)
        screen.blit(text_name, (WIDTH / 2 - 170 + 3, 390 + 3))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                init = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    Name = Name[:-1]
                elif event.key == pg.K_SPACE:
                    Name += " "
                else:
                    Name += pg.key.name(event.key)
            elif event.type == pg.MOUSEBUTTONUP:
                if (
                    (event.pos[0] > int(WIDTH / 2 - text_2.get_width() / 2))
                    and (event.pos[0] < int(WIDTH / 2 + text_2.get_width() / 2))
                    and (event.pos[1] > 480)
                    and (event.pos[1] < 480 + text_2.get_height())
                ):
                    init = False
    return Name


def join_create(screen):
    """
    Автор Дмитрий
    screen : pygame.surface - экран
    """
    font = pg.font.SysFont("Helvetica Neue", 50)
    font_medium = pg.font.SysFont("Helvetica Neue", 40)
    init = True
    WIDTH = window_width
    HEIGHT = window_height
    choice = ""
    while init:
        screen.fill((255, 255, 255))
        text_que = font.render("Who would you like to be?", False, (0, 0, 0))
        text_serv = font.render("Server", False, (0, 0, 0))
        text_cl = font.render("Client", False, (0, 0, 0))

        screen.blit(text_que, (int(WIDTH / 2 - text_que.get_width() / 2), 140))
        screen.blit(text_serv, (int(WIDTH / 2 - text_serv.get_width() / 2), 300))
        screen.blit(text_cl, (int(WIDTH / 2 - text_cl.get_width() / 2), 450))
        pg.draw.rect(
            screen,
            (0, 0, 0),
            (
                int(WIDTH / 2 - text_serv.get_width() / 2),
                300,
                text_serv.get_width(),
                text_serv.get_height(),
            ),
            2,
        )
        pg.draw.rect(
            screen,
            (0, 0, 0),
            (
                int(WIDTH / 2 - text_cl.get_width() / 2),
                450,
                text_cl.get_width(),
                text_cl.get_height(),
            ),
            2,
        )

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                init = False
                choice = "e"
            elif event.type == pg.MOUSEBUTTONUP:
                print(event.pos)
                if (
                    (event.pos[0] > int(WIDTH / 2 - text_serv.get_width() / 2))
                    and (event.pos[0] < int(WIDTH / 2 + text_serv.get_width() / 2))
                    and (event.pos[1] > 300)
                    and (event.pos[1] < 300 + text_serv.get_height())
                ):
                    init = False
                    choice = "s"
                elif (
                    (event.pos[0] > int(WIDTH / 2 - text_cl.get_width() / 2))
                    and (event.pos[0] < int(WIDTH / 2 + text_cl.get_width() / 2))
                    and (event.pos[1] > 450)
                    and (event.pos[1] < 450 + text_cl.get_height())
                ):
                    init = False
                    choice = "c"
    print(choice)
    return choice
