import pygame as pg

from constants import *

"""
Файл для отрисовки элементов

Содержит класс Drawer для отрисовки во время игры
функцию new_game для начальной заставки

Использует константы из соответствующего файла
"""


class Drawer:
    """
    Класс отрисовщика
    Функции:
    init - инициализация
    update - обновляет экран, переотрисовывает картинку
    """

    def __init__(self, screen):
        '''
        screen - экран для отрисовки
        counter - счетчик для переменной отрисовки фракталов
        direction - направление отрисовки картинки во времени для зацикливания
        '''
        self.screen = screen
        self.counter = 0
        self.direction = 1
        


    def update(self, player_tank, bullets, targets, tanks, screen, delta, IMAGES):
        '''
        player_tank - танк игрока
        bullets - массив с пулями для отрисовки
        targets - массив с целями для отрисовки
        tanks - танки для отрисовки
        screen - экран для отрисовки
        delta - промежуток времени
        IMAGES - массив с картинками для отрисовки изменяющегося фрактала
        Предполагается, что каждая имеет функцию отрисовки draw
        '''
        global window_height
        global window_width
        global fractal

        #заполнение экрана черным цветом
        self.screen.fill((0, 0, 0))

        #расчет координат для отрисовки элементов в системе танка игрока
        rect_x = world_left - player_tank.x + window_width / 2
        rect_y = world_up - player_tank.y + window_height / 2
        rect_width = world_right - world_left
        rect_height = world_down - world_up

        #белый прямоугольник - поле игры
        pg.draw.rect(self.screen, (255, 255, 255), (rect_x, rect_y, rect_width, rect_height))

        #отрисовка картинки фрактала
        pg.Surface.blit(self.screen, IMAGES[int(self.counter)], (rect_x, rect_y))

        #пополнение счетчика для дальнейшей смены картинок для прорисовки
        if self.direction == 1:
            self.counter += delta * 0.3
        else:
            self.counter -= delta * 0.3

        #условие на конец записанных картинок и смена направления отрисовки
        if self.counter >= 99:
            self.direction = 0

        #условие на конец записанных картинок и смена направления отрисовки
        if self.counter <= 0:
            self.direction = 1

        #отрисовка танка игрока
        player_tank.draw(self.screen, player_tank.x - window_width / 2, player_tank.y - window_width / 2, screen)

        #отрисовка танков из массива
        for tank in tanks:
            tank.draw(self.screen, player_tank.x - window_width / 2,  player_tank.y - window_width / 2, screen)

        #отрисовка пуль из массива
        for bullet in bullets:
            bullet.draw(self.screen, player_tank.x - window_width / 2, player_tank.y - window_width / 2)

        #отрисовка целей из массива
        for target in targets:
            target.draw(self.screen, player_tank.x - window_width / 2,  player_tank.y - window_width / 2, screen)

        pg.display.update()



def new_game(screen):
    font = pg.font.SysFont("Helvetica Neue", 50)
    font_medium = pg.font.SysFont("Helvetica Neue", 40)
    '''
    Функцию писал ДмитрийЁ видимо это окно с вводом имени
    '''
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
    return Name

def join_create(screen):
    font = pg.font.SysFont("Helvetica Neue", 50)
    font_medium = pg.font.SysFont("Helvetica Neue", 40)
    init = True
    WIDTH = window_width
    HEIGHT = window_height
    choice = ""
    while init:
        screen.fill((255, 255, 255))
        text_que = font.render("Who would you like to be?", False, (0, 0, 0))
        text_serv = font.render("Server", False, (0, 0, 0))
        text_cl = font.render("Client", False, (0, 0, 0))

        screen.blit(text_que, (int(WIDTH/2 - text_que.get_width()/2), 140))
        screen.blit(text_serv, (int(WIDTH/2 - text_serv.get_width()/2), 300))
        screen.blit(text_cl, (int(WIDTH/2 - text_cl.get_width()/2), 450))
        pg.draw.rect(screen, (0,0,0), (int(WIDTH/2-text_serv.get_width()/2),300,text_serv.get_width(),text_serv.get_height()), 2)
        pg.draw.rect(screen, (0,0,0), (int(WIDTH/2-text_cl.get_width()/2),450,text_cl.get_width(),text_cl.get_height()), 2)

        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                init = False
                choice = "e"
            elif event.type == pg.MOUSEBUTTONUP:
                print(event.pos)
                if (event.pos[0] > int(WIDTH/2 - text_serv.get_width()/2)) and (
                event.pos[0] < int(WIDTH/2 + text_serv.get_width()/2)) and (
                event.pos[1] > 300) and (event.pos[1] < 300 + text_serv.get_height()):
                    init = False
                    choice = "s"
            elif event.type == pg.MOUSEBUTTONUP:
                print(event.pos)
                if (event.pos[0] > int(WIDTH/2 - text_serv.get_width()/2)) and (
                event.pos[0] < int(WIDTH/2 + text_serv.get_width()/2)) and (
                event.pos[1] > 450) and (event.pos[1] < 450 + text_serv.get_height()):
                    init = False
                    choice = "c"
    print(choice)
    return choice
