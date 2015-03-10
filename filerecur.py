#!/usr/bin/env python

import os

folder = raw_input("Please enter the name of the path to search in")
folder = unicode(folder,"utf-8")

try:
	for cwd, dirs, files in os.walk(folder):
	
		for name in files:
			print os.path.join(cwd,name)
			print "The file statistics of %s are as shown below"%os.path.join(cwd,name)
			stats = os.stat(os.path.join(cwd,name))
			print stats.st_ctime
		for name in dirs:
			print os.path.join(cwd, name)
			
except Exception as e:
	print e
	

	


