#!/usr/bin/env python

import urllib
url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
print 'Downloading with  urllib'
urllib.urlretrieve(url,'code.zip')
