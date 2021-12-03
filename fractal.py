import pygame
import numpy as np

#surface.set_at((x, y), color)

class Fractal:
    def __init__(self, width, height, number, degree, constant):
        self.x_max = int(width / 2)
        self.y_max = int(height / 2)
        self.number = number
        self.degree = degree
        self.constant = constant
        surface = pygame.Surface((width, height))
        self.surface = surface

class Mandelbrot(Fractal):
    def __init__(self, width, height, number, degree, constant):
        super().__init__(width, height, number, degree, constant)

    def color_calculating(self, x, y):

        def color_func(iter, num):
            if iter <= num / 2:
                return int(255 * (1 - 2 * iter / num))
            else:
                return color_func(iter - num / 2, num / 2)

        x_fractal = 2 * x / self.x_max
        y_fractal = 2 * y / self.y_max

        z = x_fractal + 1j * y_fractal
        #color = (0, 0, 0)
        color = (255, 255, 255)
        for i in range(self.number):
            z = z ** (self.degree) + self.constant
            #z = z ** (2) + self.constant
            if abs(z) > 2:
                #tmp = int(255 * i / self.number)
                tmp = int(color_func(i, self.number))
                color = (tmp, tmp, tmp)
                #print(tmp, i)
                break

        return color



    def painting(self):
        for x in range(- self.x_max, self.x_max):
            for y in range(- self.y_max, self.y_max):
                color = self.color_calculating(x, y)
                self.surface.set_at((x + self.x_max, y + self.y_max), color)
