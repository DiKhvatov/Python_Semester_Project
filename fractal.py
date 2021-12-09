import pygame
import numpy as np

from constants import *

global world_left
global world_right
global world_up
global world_down

global fractal_number
global fractal_constant
global fractal_degree

#surface.set_at((x, y), color)

class Fractal:
    def __init__(self, width, height, number, degree, constant):

        def color_func(iter, num):
            if iter <= num / 2:
                return int(255 * (1 - 2 * iter / num))
            else:
                return color_func(iter - num / 2, num / 2)

        self.x_max = int(width / 2)
        self.y_max = int(height / 2)
        self.number = number
        self.degree = degree
        self.constant = constant
        surface = pygame.Surface((width, height))
        self.surface = surface
        self.colors = []

        for i in range(number):
            tmp = int(color_func(i, self.number))
            self.colors.append((tmp, tmp, tmp))

class Mandelbrot(Fractal):
    def __init__(self, width, height, number, degree, constant):
        super().__init__(width, height, number, degree, constant)

    def color_calculating(self, x, y):

        x_fractal = 2 * x / self.x_max
        y_fractal = 2 * y / self.y_max

        z = x_fractal + 1j * y_fractal
        color = (255, 255, 255)
        for i in range(self.number):
            z = z ** (self.degree) + self.constant
            #z = np.tan(z) ** self.degree + self.constant
            if abs(z) > 2:
                color = self.colors[i]
                break

        return color



    def painting(self):
        for x in range(- self.x_max, self.x_max):
            for y in range(- self.y_max, self.y_max):
                if x != 0 and y != 0:
                    color = self.color_calculating(x, y)
                    self.surface.set_at((x + self.x_max, y + self.y_max), color)


fractal = Mandelbrot(world_right - world_left, world_down - world_up, fractal_number, fractal_degree, fractal_constant)
for iter in range(100):
    fractal.constant = 0.4 + iter / 100 * 1j
    fractal.painting()
    pygame.image.save(fractal.surface, 'fractals/' + str(iter) +  '.png')
