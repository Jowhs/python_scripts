#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

payload = {'url' : 'http://www.bing.com'}
url = 'http://httpbin.org/redirect-to'
req = requests.get(url, params = payload)
print req.text
print "Response code: " + str(req.status_code)
for x in req.history:
	print str(x.status_code) + " : " + x.url
