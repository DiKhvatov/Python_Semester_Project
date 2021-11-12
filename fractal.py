import pygame

#surface.set_at((x, y), color)

class Fractal:
    def __init__(self, width, height, number):
        self.x_max = width / 2
        self.y_max = height / 2
        self.number = number

class Mandelbrot(Fractal):
    def __init__(self, width, height, number):
        super().__init__(width, height, number)
