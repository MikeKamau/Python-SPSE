#!/usr/bin/env python

import SocketServer

class EchoHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print "Got Connection from: ", self.client_address
		data = 'mikey'
		
		while len(data):
			data = self.request.recv(1024)
			print "Client sent: " + data
			self.request.send(data)
		
		print "Client left"
		self.request.close()

serverAddr = ('0.0.0.0',9000) 
server = SocketServer.TCPServer(serverAddr, EchoHandler)
server.serve_forever()