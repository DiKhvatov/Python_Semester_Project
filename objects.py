import numpy as np
import pygame as pg


class Bullet:
    def __init__(self, x, y, shooting_angle, v):
        self.x = x
        self.y = y
        self.angle = shooting_angle
        self.v = v
        self.existion = True

    def checking_breakthrough(self, tanks):
        for tank in tanks:
            distance = np.sqrt((self.x - tank.x) ** 2 + (self.y - tank.y) ** 2)
            if tank.r > distance:
                tank.breakthrough()
                self.existion = False


class Tank:
    """
    Класс танка
    x,y - координаты
    angle - угол поворота в двумерном пространстве
    v, a - скороть и ускорение вдоль направления танка
    r - радиус танка, пока мы не решили вопрос с его отрисовкой
    color - цвет танка

    Надо доделать отрисовку на поверхность, которую будем поворачивать и рисовать на основной экран
    """

    def __init__(self):
        """
        инициализация
        """
        self.x = 0
        self.y = 0
        self.v = 0
        self.a = 0
        self.angle = 0
        self.r = 5
        self.color = (255, 255, 255)

    def move(self, delta):
        """
        Изменения скорости, координат и угла поворота за малое время delta
        """
        self.v += self.a * delta
        self.x += self.v * delta * np.cos(angle)
        self.y += self.v * delta * np.sin(angle)
        self.angle += self.w * delta

    def start_acceleration_forward(self, acceleration):
        """
        Предположительно мы нажимаем стрелочку вперед и запускаем эту функцию, но теперь мне кажется это немного туповатым
        """
        self.a = acceleration

    def start_acceleration_back(self, acceleration):
        self.start_acceleration_forward(-acceleration)

    def end_acceleration_forward(self, acceleration):
        self.a = 0

    def end_acceleration_back(self, acceleration):
        self.start_acceleration_forward(-acceleration)

    def start_rotate_right(self, w):
        self.w = w

    def end_rotate_right(self, w):
        self.w = 0

    def start_rotate_left(self, w):
        self.w = w

    def end_rotate_left(self, w):
        self.w = 0

    def draw(self, surface):
        # TODO: что-то мне лень пока что
        pass


class Target:
    def __init__(self):
        # TODO: класс
        self.x = 0
        self.y = 0


class Target_shooting(Target):
    def __init__(self):
        super().__init__(self)
        self.shooting_angle = 0

    def aiming(self, tank):
        distance = np.sqrt((self.x - tank.x) ** 2 + (self.y - tank.y) ** 2)
        self.shooting_angle = np.arctan((tank.x - self.x) / distance)

    def shoot(self):
        return Bullet(self.x, self.y, self.shooting_angle, 10)
