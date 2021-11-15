import pygame as pg
import thorpy

window_height = 1000
window_width = 1000

"""
Есть идея засунуть все связанное с рисованием в этот файл
"""


class Drawer:
    """
    Стыренная функция из проекта солнечной системы
    Надо бы
    """

    def __init__(self, screen):
        self.screen = screen

    def update(self, figures, ui):
        self.screen.fill((0, 0, 0))
        for figure in figures:
            figure.draw(self.screen)

        ui.blit()
        ui.update()
        pg.display.update()


def init_ui(screen):

    button_stop = thorpy.make_button("Quit", func=stop_execution)
    button_pause = thorpy.make_button("Pause", func=pause_execution)
    button_play = thorpy.make_button("Play", func=start_execution)
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
