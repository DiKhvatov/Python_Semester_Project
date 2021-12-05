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
fractal.painting()

class Drawer:
    """
    Стыренная функция из проекта солнечной системы
    Надо бы
    """

    def __init__(self, screen):
        self.screen = screen

    def update(self, player_tank, bullets, targets, tanks, ui, screen):

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

        pygame.Surface.blit(self.screen, fractal_surface, (rect_x, rect_y))
        #pygame.Surface.blit(self.screen, fractal_surface, (0,0))

        player_tank.draw(self.screen, player_tank.x - window_width / 2, player_tank.y - window_width / 2, screen)

        for tank in tanks:
            tank.draw(self.screen, player_tank.x - window_width / 2,  player_tank.y - window_width / 2, screen)

        for bullet in bullets:
            bullet.draw(self.screen, player_tank.x - window_width / 2, player_tank.y - window_width / 2)

        for target in targets:
            target.draw(self.screen, player_tank.x - window_width / 2,  player_tank.y - window_width / 2, screen)


        ui.blit()
        ui.update()
        pg.display.update()


def stop_execution():

    pass

def pause_execution(delta):
    delta = 0
    pass

def start_execution():
    pass

def new_game():
    pass




def init_ui(screen):
    '''
    Инициализация графического интерфейса
    '''
    button_stop = thorpy.make_button("Quit", func=stop_execution)
    button_pause = thorpy.make_button("Pause", func=pause_execution)
    button_play = thorpy.make_button("Play", func=start_execution)
    timer = thorpy.OneLineText("Time: ")
    rounds = thorpy.OneLineText("Round: ")
    score = thorpy.OneLineText("Score: ")
    button_new_game = thorpy.make_button(text="New game", func=new_game)

    box = thorpy.Box(
        elements=[button_pause, button_stop, button_play, button_new_game, timer, score]
    )

    menu = thorpy.Menu(box)
    for element in menu.get_population():
        element.surface = screen

    box.set_topleft((0, 0))
    box.blit()
    box.update()
    return menu, box, rounds, score
