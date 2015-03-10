#!/usr/bin/env python

import SocketServer
import SimpleHTTPServer

class HTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
		def do_GET(self):
			if self.path == '/admin':
				self.wfile.write("You are accessing the admin console\n\n\n")
				self.wfile.write(self.headers)
			else:
				SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
		
	
	
http_server = SocketServer.TCPServer(('',9000),HTTPRequestHandler)
http_server.serve_forever()