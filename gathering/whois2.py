#!usr/bin/python
# -*- coding: utf-8 -*-

import pythonwhois
import sys

if len(sys.argv) == 1:
	print "Introduzca un objetivo: "
elif len(sys.argv) > 3:
	print "El máximo de objetivos son 2"
elif len(sys.argv) == 2 or len(sys.argv) == 3:
	whois = pythonwhois.get_whois(sys.argv[1]) # opción whois del módulo whois, recibirá como argumento el nombre del dominio$
	for key in whois.keys():
        	print "[+] %s : %s \n" %(key, whois[key]) # recorremos el diccionario
