import socket
import time
import threading

class Server:
	def __init__(self):
		self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
		print("Server is created")
		
		self.IP = (socket.gethostbyname_ex(socket.gethostname())[2])[0]
		print (self.IP)

		self.serv.bind((IP, PORT))
		self.serv.listen()

		





