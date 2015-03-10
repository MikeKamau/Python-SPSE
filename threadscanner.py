#!/usr/bin/env python

import logging
import argparse
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import threading
conf.verb = 0

host = 'localhost'
start_port = 1
end_port = 1024


def user_input():
	
	global host
	global start_port
	global end_port
	
	#here is where we collect the ip address and ports to scan
	parser = argparse.ArgumentParser(description="This is a network port scanner")
	parser.add_argument('-s', help='enter the host to scan', type=str)
	parser.add_argument('-r', help='enter the range of ports to scan eg 1-20', type=str)
	input_string = parser.parse_args()
	host = input_string.s
	ports = input_string.r
	
	#here is where we get the obtain the start and end ports to scan from the user input
	if ports == None:
		print 'Type "./threadscanner.py -h" to get usage information'
		exit(1)
	else:
		port_list = map(int,ports.split('-'))
		start_port = port_list[0]
		end_port = port_list[len(port_list)-1]
	
def scanner(hst, port):
	try:
		response = sr1(IP(dst=hst)/TCP(dport=port, flags= 'S'), timeout=1)
		if  response is None:
			print "This port %d is closed"%port
		elif(response.haslayer(TCP)):
			if(response.getlater(TCP).flags == 0x12):
				print "Port %d is open"%port
				sr(IP(dst=hst)/TCP(dport=port, flags='AR'), timeout=1)
			elif(response.getlayer(TCP).flags == 0x14):
				print "Port %d is closed"%port
		else:
			print "Port in unkown state"
	except:
		print "Error occurred with packets" 
		
		
			
			
def main():
	global host
	user_input()
	for port in range(start_port, end_port + 1):
		scan_thread = threading.Thread(target=scanner, args=(host,port))
		scan_thread.start()	
		
		
if __name__ == '__main__':
	main()		
