#!/usr/bin/env python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0',9000))
server.listen(1)
client, addr = server.accept()
if client:
	print "Enter a message that will be repeated to you"
	message = client.recv(4096)
	client.send(message)
	client.close()
	server.close()
else:
	print "There was an error receiving or sending with client"
	client.close()
	server.close()
	