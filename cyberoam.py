#!/usr/bin/env python2
# Author: mOoDyGuY

import urllib
import time

#student ID without '@d-iict.org'
username = '201321008'

#cyberoam password
password = 'passwordhere'

#relogin time period in minutes
tm = 120

while True:
	try:
		f = urllib.urlopen('https://10.100.56.55:8090/httpclient.html','mode=191&username='+username+'&password='+password)
		s = f.read()
		f.close()
		s=s.split('message')[1][10:-5]
		print time.strftime('--%Y-%m-%d %I:%M %p--'), s+'.'
		time.sleep (tm*60)
	except IOError, error:
		print time.strftime('--%Y-%m-%d %I:%M %p--'), str(error)

