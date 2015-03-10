#!/usr/bin/env python

import socket
import threading

def thread_handler(client_socket):
	client_socket.send('Enter the message you want repeated to you')
	message = client_socket.recv(4096)
	client_socket.send(message)
	client_socket.close()
	return

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0',9000))
server.listen(10)

while True:
	client, addr = server.accept()
	client_thread = threading.Thread(target=thread_handler, args=(client,))
	client_thread.start()