#!/usr/bin/env python

import socket
import multiprocessing
import sys

def process_handler(client_socket):
	client_socket.send('Enter the message you want repeated to you')
	message = client_socket.recv(4096)
	client_socket.send(message)
	client_socket.shutdown(socket.SHUT_RDWR)
	client_socket.close()
	sys.exit(0)
	
if __name__ == '__main__':
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind(('0.0.0.0',9000))
	server.listen(10)
	jobs = []
	while True:
		client, addr = server.accept()
		client_process = multiprocessing.Process(target=process_handler, args=(client,))
		client_process.daemon = True		
		jobs.append(client_process)		
		client_process.start()
