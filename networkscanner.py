#!/usr/bin/env python


import logging
import argparse
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

#this line is to suppress the verbosity of scapy's send functions
conf.verb = 0

#this is the function that does the actual scanning of the ports
def scanner(hst, startport, endport):
	for port in range(startport, endport):
		response = sr1(IP(dst=hst)/TCP(dport=port, flags= 'S'), timeout=1)
		if  response is None:
			print "This port is closed"
		elif(response.haslayer(TCP)):
			if(response.getlater(TCP).flags == 0x12):
				print "Port %d is open"%port
				sr(IP(dst=hst)/TCP(dport=port, flags='AR'), timeout=1)
			elif(response.getlayer(TCP).flags == 0x14):
				print "Port %d is closed"%port
		else:
			print "Port in unkown state" 

#here is where we collect the ip address and ports to scan
parser = argparse.ArgumentParser(description="This is a network port scanner")
parser.add_argument('-s', help='enter the host to scan', type=str)
parser.add_argument('-r', help='enter the range of ports to scan eg 1-20', type=str)
input_string = parser.parse_args()
host = input_string.s
ports = input_string.r

#here is where we get the obtain the start and end ports to scan from the user input
port_list = map(int,ports.split('-'))
start_port = port_list[0]
end_port = port_list[len(port_list)-1]


scanner(host, start_port, end_port + 1)












