import socket
import time
import threading


def thread_messages(nick, con, adr):
	
	con.send(str.encode('Welcome to the dungeon'))

	while True:
		try:
			message = con.recv(2048).decode()
			if message:
				print("<" + nick + "> " + message)
				broadcast(message, con, nick)
			else:
				continue
		except:
			continue

def broadcast(message, conn, nick):
	for nickname, client in list_of_clients.items():
		if client != conn:
			try:
				client.send(str.encode("<" + nick + "> " + message))
			except:
				client.close()
				list_of_clients.remove(client)
				print(len(list_of_clients))
		if client == conn:
			try:
				client.send(str.encode("<" + "You" + "> " + message))
			except:
				client.close()
				list_of_clients.remove(client)
				print(len(list_of_clients))

def remove(connection):
	if connection in list_of_clients.items():
		list_of_clients.remove(connection)



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Server is created")

IP = "172.20.10.2"
PORT = 5050
list_of_clients = {}

server.bind((IP, PORT))
server.listen()

print("Connection extablished")

while True:
	conn, addr = server.accept()
	nick = conn.recv(2048).decode()
	list_of_clients[nick] = conn

	threading.Thread(target = thread_messages, args = (nick, conn, addr)).start()



server.close()



