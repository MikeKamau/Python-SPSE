#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib

url = 'http://slashdot.org'
html = urllib.urlopen(url)
bs = BeautifulSoup(html.read(),"lxml")
print "Stories on Slashdot\'s front page are"
stories = bs.find_all('a','a')
print stories


