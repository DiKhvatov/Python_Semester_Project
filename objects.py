import numpy as np
import pygame as pg
from constants import *

global world_left
global world_right
global world_up
global world_down

class Bullet:
    '''

    '''
    def __init__(self, x, y, shooting_angle, v, parent):
        self.x = x
        self.y = y
        self.angle = shooting_angle
        self.v = v
        self.existion = True
        self.counter = 0
        self.color = (0,0,255)
        self.r = 5
        self.parent = parent

    def checking_breakthrough(self, tanks):
        for tank in tanks:
            distance = np.sqrt((self.x - tank.x) ** 2 + (self.y - tank.y) ** 2)
            if tank.r > distance:
                tank.breakthrough()
                self.existion = False

    def move(self, delta):
        self.x += self.v * np.cos(self.angle) * delta
        self.y += self.v * np.sin(self.angle) * delta

    def draw(self, surface, x, y):
        pg.draw.circle(surface, self.color, (self.x - x, self.y - y), self.r)

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

    def move(self, delta):
        """
        Изменения скорости, координат и угла поворота за малое время delta
        """
        self.v += self.a * delta
        self.x += self.v * delta * np.cos(self.angle)
        self.y += self.v * delta * np.sin(self.angle)
        self.angle += self.w * delta


    def draw(self, surface, x, y, screen):
        image = pg.image.load('floppa.png').convert_alpha()
        new_image = pg.transform.scale(image, (2*self.r, 2*self.r))
        new_image = pg.transform.rotate(new_image, -90 - 180*self.angle/np.pi)
        screen.blit(new_image, (self.x - x - 1.2*self.r, self.y - y - 1.2*self.r))



    def wall_collision(self, delta):
        if self.x > world_right or self.x < world_left or self.y > world_down or self.y < world_up:
            self.health += -0.1 * delta
            print(self.health)



    def breakthrough(self):
        self.health += -1
        if self.health <= 0:
            self.existion = False

class Target:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.v = v
        self.a = 0
        self.w = 0
        self.angle = 0
        self.r = 50
        self.color = (255, 255, 0)
        self.color_2 = (255, 0, 0)
        self.health = 25
        self.type = "simple target"
        self.existion = True


    def aiming(self, tank):
        distance = np.sqrt((self.x - tank.x) ** 2 + (self.y - tank.y) ** 2)
        self.angle = np.arccos((tank.x - self.x) / distance)

        if -(self.y - tank.y) < 0:
            self.angle = 2 * np.pi - self.angle

    def breakthrough(self):
        self.health += -1
        if self.health <= 0:
            self.existion = False

    def move(self, delta):
        """
        Изменения скорости, координат и угла поворота за малое время delta
        """
        self.v += self.a * delta
        self.x += self.v * delta * np.cos(self.angle)
        self.y += self.v * delta * np.sin(self.angle)
        self.angle += self.w * delta

    def draw(self, surface, x, y, screen):
        image = pg.image.load('floppa2.png').convert_alpha()
        new_image = pg.transform.scale(image, (2*self.r, 2*self.r))
        new_image = pg.transform.rotate(new_image, -90 - 180*self.angle/np.pi)
        screen.blit(new_image, (self.x - x - 1.2*self.r, self.y - y - 1.2*self.r))

class Target_shooting(Target):
    def __init__(self, x, y, v):
        super().__init__(x, y, v)
        self.shooting_angle = 0
        self.charge = 10
        self.type = "shooting target"

    def shoot_aiming(self, tank):
        distance = np.sqrt((self.x - tank.x) ** 2 + (self.y - tank.y) ** 2)
        self.shooting_angle = np.arccos((tank.x - self.x) / distance)

        if -(self.y - tank.y) < 0:
            self.shooting_angle = 2 * np.pi - self.shooting_angle

    def charging(self, delta):
        self.charge += delta


    def shoot(self):
        if self.charge >= 10:
            self.charge = 0
            return Bullet(self.x, self.y, self.angle, 10, "target")
        return 0
