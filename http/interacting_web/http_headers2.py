#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
myheaders = {'user-agent' : 'iPhone6'} # Falsificamos la opción user-agent del headers, en este caso simulamos estar en un iPhone6
r = requests.get("http://httpbin.org/headers", headers = myheaders)
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

