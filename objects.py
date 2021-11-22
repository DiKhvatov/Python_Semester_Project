import numpy as np
import pygame as pg


class Bullet:
    '''

    '''
    def __init__(self, x, y, shooting_angle, v):
        self.x = x
        self.y = y
        self.angle = shooting_angle
        self.v = v
        self.existion = True
        self.counter = 0
        self.color = (0,0,255)
        self.r = 5

    def checking_breakthrough(self, tanks):
        for tank in tanks:
            distance = np.sqrt((self.x - tank.x) ** 2 + (self.y - tank.y) ** 2)
            if tank.r > distance:
                tank.breakthrough()
                self.existion = False

    def move(self, delta):
        self.x += self.v * np.cos(self.angle) * delta
        self.y += self.v * np.sin(self.angle) * delta

    def draw(self, surface):
        pg.draw.circle(surface, self.color, (self.x, self.y), self.r)

    def wall_collision(self, wall_x_left, wall_x_right, wall_y_up, wall_y_down):
        if self.x < wall_x_left or self.x > wall_x_right or self.y < wall_y_up or self.y > wall_y_down:
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
        self.w = 0
        self.angle = 0
        self.r = 50
        self.color = (0, 255, 0)
        self.color_2 = (255, 0, 0)

    def move(self, delta):
        """
        Изменения скорости, координат и угла поворота за малое время delta
        """
        self.v += self.a * delta
        self.x += self.v * delta * np.cos(self.angle)
        self.y += self.v * delta * np.sin(self.angle)
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
        pg.draw.circle(surface, self.color, (self.x, self.y), self.r)
        pg.draw.circle(surface, self.color_2, (self.x + self.r * np.cos(self.angle) , self.y+ self.r * np.sin(self.angle) ), self.r / 5)


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
