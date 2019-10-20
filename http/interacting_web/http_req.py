#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

url = "http://httpbin.org/html"
req = requests.get(url)
print "Response code: " + str(req.status_code)
