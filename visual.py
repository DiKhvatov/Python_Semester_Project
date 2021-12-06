import pygame as pg
import thorpy

from constants import *
from fractal import *

global window_height
global window_width

global world_left
global world_right
global world_up
global world_down

global fractal_number
global fractal_constant
global fractal_degree

"""
Есть идея засунуть все связанное с рисованием в этот файл
"""

fractal = Mandelbrot(world_right - world_left, world_down - world_up, fractal_number, fractal_degree, fractal_constant)
#fractal.painting()

class Drawer:
    """
    Стыренная функция из проекта солнечной системы
    Надо бы
    """

    def __init__(self, screen):
        self.screen = screen

    def update(self, player_tank, bullets, targets, tanks, screen):

        global window_height
        global window_width
        global fractal

        self.screen.fill((0, 0, 0))
        fractal_surface = fractal.surface


        rect_x = world_left - player_tank.x + window_width / 2
        rect_y = world_up - player_tank.y + window_height / 2
        rect_width = world_right - world_left
        rect_height = world_down - world_up

        pg.draw.rect(self.screen, (255, 255, 255), (rect_x, rect_y, rect_width, rect_height))

        pg.Surface.blit(self.screen, fractal_surface, (rect_x, rect_y))
        #pygame.Surface.blit(self.screen, fractal_surface, (0,0))

        player_tank.draw(self.screen, player_tank.x - window_width / 2, player_tank.y - window_width / 2, screen)

        for tank in tanks:
            tank.draw(self.screen, player_tank.x - window_width / 2,  player_tank.y - window_width / 2, screen)

        for bullet in bullets:
            bullet.draw(self.screen, player_tank.x - window_width / 2, player_tank.y - window_width / 2)

        for target in targets:
            target.draw(self.screen, player_tank.x - window_width / 2,  player_tank.y - window_width / 2, screen)

        pg.display.update()


pg.init()

font = pg.font.SysFont("Helvetica Neue", 50)
font_medium = pg.font.SysFont("Helvetica Neue", 40)

def new_game(screen):
    init = True
    Name = ""
    WIDTH = window_width
    HEIGHT = window_height
    while init:
        screen.fill((255, 255, 255))
        text_1 = font.render("Enter your name", False, (0, 0, 0))
        text_2 = font.render("Submit", False, (0, 0, 0))
        text_name = font_medium.render(Name, False, (0, 0, 0))
        pg.draw.rect(screen, (0,0,0), (int(WIDTH/2 - 3 - text_2.get_width()/2), 480-3, text_2.get_width() + 6, text_2.get_height() + 6), 2)
        screen.blit(text_1, (int(WIDTH/2 - text_1.get_width()/2), 270))
        screen.blit(text_2, (int(WIDTH/2 - text_2.get_width()/2), 480))
        pg.draw.rect(screen, ((0, 0, 0)), (WIDTH/2 - 170, 390, 340, 50), 2)
        screen.blit(text_name, (WIDTH/2 - 170 + 3, 390 + 3))
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
                if (event.pos[0] > int(WIDTH/2 - text_2.get_width()/2)) and (
                event.pos[0] < int(WIDTH/2 + text_2.get_width()/2)) and (
                event.pos[1] > 480) and (event.pos[1] < 480 + text_2.get_height()):
                    init = False
    print(Name)
    return Name












