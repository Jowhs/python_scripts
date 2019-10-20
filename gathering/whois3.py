#! /usr/bin/python
# -*- coding:utf-8 -*-

import pythonwhois
import sys

if len(sys.argv) != 2:
	print "Introduce un 2 nombres de dominio: "
	sys.exit()

domain = pythonwhois.get_whois(sys.argv[1])
for key in domain.keys():
	print "* %s : %s \n" %(key, domain[key])
