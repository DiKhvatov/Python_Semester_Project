import numpy as np
import pygame as pg

class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.v = 0
        self.a = 0
        self.angle = 0
        self.r = 5
        self.color = (255,255,255)

    def move(self, delta):
        self.v += self.a * delta
        self.x += self.v * delta * np.cos(angle)
        self.y += self.v * delta * np.sin(angle)
        self.angle += self.w * delta

    def start_acceleration_forward(self, acceleration):
        self.a = acceleration

    def start_acceleration_back(self, acceleration):
        self.start_acceleration_forward(- acceleration)

    def end_acceleration_forward(self, acceleration):
        self.a = 0

    def end_acceleration_back(self, acceleration):
        self.start_acceleration_forward(- acceleration)

    def start_rotate_right(self, w):
        self.angle = w

    def end_rotate_right(self, w):
        self.angle = 0

    def start_rotate_left(self, w):
        self.angle = w

    def end_rotate_left(self, w):
        self.angle = 0

    def draw(self, screen):
        # TODO: надо как-нибудь классненько с поворотами
        pass
