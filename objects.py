import numpy as np
import pygame as pg
from constants import *


"""
Файл с описание классов элементов
Bullet - класс пуль
Tank - класс танков
Target - класс цели
Target_shooting - класс стреляющей цели с наследованием от простого класса цели
"""


class Bullet:
    """
    Класс пули
    """

    def __init__(self, x, y, shooting_angle, v, parent):
        """
        Инициализация
        x, y : float - положение пули
        angle : float - направление движения
        v : float - скорость пули
        existion : bool - флаг существования пули с неправильным написанием
        color : list - цвет пули
        r : float - размер пулм
        parent : string - метка класса создателя пули, чтобы она этот класс не трогала
        """
        self.x = x
        self.y = y
        self.angle = shooting_angle
        self.v = v
        self.existion = True
        self.counter = 0
        self.color = (0, 0, 255)
        self.r = 5
        self.parent = parent

    def checking_breakthrough(self, tanks):
        """
        функция проверки столкновения с элементами из массива
        tanks : massive - массив с танками
        """
        for tank in tanks:
            distance = np.sqrt((self.x - tank.x) ** 2 + (self.y - tank.y) ** 2)
            if tank.r > distance:
                tank.breakthrough()
                self.existion = False

    def move(self, delta):
        """
        Функция перемещения пули за время delta
        delta : float
        """
        self.x += self.v * np.cos(self.angle) * delta
        self.y += self.v * np.sin(self.angle) * delta

    def draw(self, surface, x, y):
        """
        Функция отрисовки пули на поверхности в системе отсчета танка игрока
        surface : Pygame.surface - поверхность для отрисовки
        x,y : float- подающиеся координаты
        """
        pg.draw.circle(surface, self.color, (self.x - x, self.y - y), self.r)

    def wall_collision(self, wall_x_left, wall_x_right, wall_y_up, wall_y_down):
        """
        Проверка на выход пуль за пределы карты
        wall_x_left, wall_x_right, wall_y_up, wall_y_down : float
        """
        if (
            self.x < wall_x_left
            or self.x > wall_x_right
            or self.y < wall_y_up
            or self.y > wall_y_down
        ):
            self.existion = False


class Tank:
    """
    Класс танка
    """

    def __init__(self):
        """
        инициализация
        x,y : float - координаты
        v, a : float - скорость и ускорение
        w : float - частота вращения
        angle : float - угол поворота
        r : float - радиус
        color, color_2 : list - цвета для отрисовки элементов танка
        health : float - здоровье танка
        existion : bool - флаг существования
        image : pygame.surface - картинка танка
        """
        self.x = 200
        self.y = 200
        self.v = 0
        self.a = 0
        self.w = 0
        self.angle = 0
        self.r = 50
        self.color = (0, 255, 0)
        self.color_2 = (255, 0, 0)
        self.health = 100
        self.existion = True
        self.image = pg.image.load("images/Tank.png").convert_alpha()

    def move(self, delta):
        """
        Изменения скорости, координат и угла поворота за малое время delta
        delta : float
        """
        self.v += self.a * delta
        self.x += self.v * delta * np.cos(self.angle)
        self.y += self.v * delta * np.sin(self.angle)
        self.angle += self.w * delta
        while self.angle >= 2 * np.pi:
            self.angle += -2 * np.pi
        while self.angle < 0:
            self.angle += 2 * np.pi

    def draw(self, surface, x, y, screen):
        """
        Отрисовка картинки танка
        автор - Батухан
        surface : pygame.surface - поверхность для отрисовки туда танка
        x, y : float - координаты для отрисовки с учетом смещения
        """
        image = self.image
        new_image = pg.transform.scale(image, (2 * self.r, 2 * self.r))
        new_image = pg.transform.rotate(new_image, -90 - 90 - 180 * self.angle / np.pi)
        rot = self.angle
        while rot >= np.pi / 2:
            rot += -np.pi / 2
        deltaX = (
            self.r * np.sqrt(2) * np.cos(np.pi / 4 + rot)
            + 2 * np.sin(rot) * self.r
            - self.r
        )
        deltaY = self.r * np.sin(np.pi / 4 + rot) - self.r
        screen.blit(
            new_image,
            (self.x - x - 1.2 * self.r - deltaX, self.y - y - 1.2 * self.r - deltaY),
        )
        pg.draw.rect(screen, (255, 0, 0), (self.x - x - 50, self.y - y - self.r, self.health, 5))

    def wall_collision(self, delta):
        """
        Просчет выхода танка за границы мира и уменьшение его здоровья
        delta : float - промежуток времени
        """
        if (
            self.x > world_right
            or self.x < world_left
            or self.y > world_down
            or self.y < world_up
        ):
            self.health += -0.1 * delta

    def breakthrough(self):
        """
        Функция, сообщающая танку, что в него попала пуля
        """
        self.health += -1
        if self.health <= 0:
            self.existion = False

    def new_round(self):
        """
        Обновление координат и скорости при начале нового раунда
        """
        self.x = 0
        self.y = 0
        self.v = 0

    def target_collision(self, target):
        """
        Проверка, сталкивается ли танк с целями
        target : class Target - цель
        """
        if (self.x - target.x) ** 2 + (self.y - target.y) ** 2 <= (
            self.r + target.r
        ) ** 2:
            self.health -= 10
            target.existion = False


class Target:
    """
    Класс цели
    """

    def __init__(self, x, y, v):
        """
        инициализация
        x,y : float - координаты
        v, a : float - скорость и ускорение
        w : float - частота вращения
        angle : float - угол поворота
        r : float - радиус
        color, color_2 : list - цвета для отрисовки элементов танка
        health : float - здоровье танка
        existion : bool - флаг существования
        image : pygame.surface - картинка танка
        """
        self.x = x
        self.y = y
        self.v = v
        self.a = 0
        self.w = 0
        self.angle = 0
        self.r = 50
        self.color = (255, 255, 0)
        self.color_2 = (255, 0, 0)
        self.health = 5
        self.type = "simple target"
        self.existion = True
        self.image = pg.image.load("images/tank1.png").convert_alpha()

    def aiming(self, tank):
        """
        Высокоинтелеллектуальный алгоритм преследования танка
        tank : class Tank
        """
        distance = np.sqrt((self.x - tank.x) ** 2 + (self.y - tank.y) ** 2)
        self.angle = np.arccos((tank.x - self.x) / distance)

        if -(self.y - tank.y) < 0:
            self.angle = 2 * np.pi - self.angle

    def breakthrough(self):
        """
        Сообщение цели, что в нее попала пуля
        """
        self.health += -1
        if self.health <= 0:
            self.existion = False

    def move(self, delta):
        """
        Изменения скорости, координат и угла поворота за малое время delta
        delta : float
        """
        self.v += self.a * delta
        self.x += self.v * delta * np.cos(self.angle)
        self.y += self.v * delta * np.sin(self.angle)
        self.angle += self.w * delta

    def draw(self, surface, x, y, screen):
        """
        Функция отрисовки цели
        автор - Батухан
        x, y : float - координаты для смещения
        surface, screen : pygame.surface - Батухан идиот - испотрил функцию, времени фиксит до сдачи не остается
        """
        image = self.image
        new_image = pg.transform.scale(image, (2 * self.r, 2 * self.r))
        new_image = pg.transform.rotate(new_image, 180 -90 - 180 * self.angle / np.pi)
        screen.blit(new_image, (self.x - x - 1.2 * self.r, self.y - y - 1.2 * self.r))


class Target_shooting(Target):
    """
    Класс стреляющей цели с наследованием от обычной
    """

    def __init__(self, x, y, v):
        """
        Инициализация
        shooting_angle : float - угол направления башни цели
        charge : float - заряд пушки для стрельбы
        type : string - тип цели чтобы различать стреляющую и обычную
        """
        super().__init__(x, y, v)
        self.shooting_angle = 0
        self.charge = 10
        self.type = "shooting target"

    def shoot_aiming(self, tank):
        """
        Высокоинтелеллектуальный способ прицеливания в данный танк
        tank : class Tank - данный танк
        """
        distance = np.sqrt((self.x - tank.x) ** 2 + (self.y - tank.y) ** 2)
        self.shooting_angle = np.arccos((tank.x - self.x) / distance)

        if -(self.y - tank.y) < 0:
            self.shooting_angle = 2 * np.pi - self.shooting_angle

    def charging(self, delta):
        """
        Зарядка для последующего выстрела
        delta : float
        """
        self.charge += delta

    def shoot(self):
        """
        Выстрел
        """
        global v_bullet
        if self.charge >= 50:
            self.charge = 0
            slap = pg.mixer.Sound("music/slap7.ogg")
            slap.play()
            return Bullet(self.x, self.y, self.angle, v_bullet, "target")
        return 0
