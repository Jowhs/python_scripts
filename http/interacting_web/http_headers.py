#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

r = requests.head("http://httpbin.org/ip") #Hemos cambiado get por head para obtener sólo las cabeceras
print r.url
print "Status code: "
print "\t [*]" + str(r.status_code) + "\n"

print "Server headers"
print "============================================"
for x in r.headers:
	print "\t" + x + " : " + r.headers[x]
print "============================================"

print "Content:\n"
print r.text
