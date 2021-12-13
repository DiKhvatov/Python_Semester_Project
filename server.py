import socket
import time
import threading
import pygame as pg

from constants import *

class Server:
	def __init__(self):
		self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.list_of_clients = {}
		self.PORT = 0
		print("Initialization")
		
		self.IP = (socket.gethostbyname_ex(socket.gethostname())[2])[0]
		print ("Your IP is " + str(self.IP))

	def bind(self):
		self.serv.bind((self.IP, self.PORT))
		self.serv.listen()
		print("Waiting for connections")

	def enter_port(self, screen):
		font = pg.font.SysFont("Helvetica Neue", 50)
		font_medium = pg.font.SysFont("Helvetica Neue", 40)
		init = True
		port = ""
		WIDTH = window_width
		HEIGHT = window_height
		while init:
			screen.fill((255, 255, 255))
			text_1 = font.render("Enter Port number", False, (0, 0, 0))
			text_rec = font_medium.render("(Recommended 49152-65535)", False, (0, 0, 0))
			text_2 = font.render("Submit", False, (0, 0, 0))
			text_port = font_medium.render(port, False, (0, 0, 0))
			pg.draw.rect(screen, (0,0,0), (int(WIDTH/2 - 3 - text_2.get_width()/2), 480-3, text_2.get_width() + 6, text_2.get_height() + 6), 2)
			screen.blit(text_1, (int(WIDTH/2 - text_1.get_width()/2), 200))
			screen.blit(text_rec, (int(WIDTH/2 - text_rec.get_width()/2), 270))
			screen.blit(text_2, (int(WIDTH/2 - text_2.get_width()/2), 480))
			pg.draw.rect(screen, ((0, 0, 0)), (WIDTH/2 - 170, 390, 340, 50), 2)
			screen.blit(text_port, (WIDTH/2 - 170 + 3, 390 + 3))
			pg.display.update()
			for event in pg.event.get():
				if event.type == pg.QUIT:
					init = False
				elif event.type == pg.KEYDOWN:
					if event.key == pg.K_BACKSPACE:
						port = port[:-1]
					elif event.key == pg.K_SPACE:
						port += " "
					else:
						port += pg.key.name(event.key)
				elif event.type == pg.MOUSEBUTTONUP:
					if (event.pos[0] > int(WIDTH/2 - text_2.get_width()/2)) and (
					event.pos[0] < int(WIDTH/2 + text_2.get_width()/2)) and (
					event.pos[1] > 480) and (event.pos[1] < 480 + text_2.get_height()):
						init = False
		print("Your port is now " + str(port))
		self.PORT = int(port)



