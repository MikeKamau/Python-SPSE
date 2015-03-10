#!/usr/bin/env python

import socket
import signal
import sys
import argparse

def signal_handler(signum, frame):
	sys.exit(0)
	
	
#this is where we take the timeout value for the server
parser = argparse.ArgumentParser()
parser.add_argument('-t', help='This is the number of seconds the server will stay up before timing out', type=int)
rcvd_input = parser.parse_args()
seconds = rcvd_input.t



#this is where we install the signal handler

signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(seconds)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',9000))
server.listen(5)
client, addr = server.accept()
client.recv(1024)
client.send('ACK')
client.close()
	