#!/usr/bin/env python

import SocketServer
import threading

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
		

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass
	
server_thread = ThreadedTCPServer(('0.0.0.0', 9000), EchoHandler)
server_thread.serve_forever()