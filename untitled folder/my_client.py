import socket
import time
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = "172.20.10.2"
PORT = 5050

server.connect((IP, PORT))
print("Connection established")

nickname = input("Enter your nickname: ")

server.send(nickname.encode())

def recieve():

	while True:
		try:
			message = server.recv(2048).decode()
			if message:
				print(message)
		except:
			continue


def sending():

	while True:
		try:
			message_to_send = input()		
			server.send(message_to_send.encode())
		except:
			continue


threading.Thread(target=recieve).start()
threading.Thread(target=sending).start()
