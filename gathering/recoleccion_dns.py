#!usr/bin/python
# -*- coding: utf-8 -*-

import dns
import dns.resolver
import dns.exception
import dns.query

obj = raw_input("Introduzca el nombre del objetivo: ")

ansA = dns.resolver.query(obj, 'A')
ansMX = dns.resolver.query(obj, 'MX')
ansNS = dns.resolver.query(obj, 'NS')
ansSOA = dns.resolver.query(obj, 'SOA')
ansTXT = dns.resolver.query(obj, 'TXT')

print "**********************"
 
print "Información sobre IPv4:"
for ans in ansA:
	print "[-]", ans

print "**********************"

print "Información sobre servidores de correo:"
for ans in ansMX:
	print "[-]", ans

print "**********************"

print "Información sobre nombres de servidores:"
for ans in ansNS:
	print "[-]", ans

print "**********************"

print "Información sobre IPv6:"

try:
	ansAAAA = dns.resolver.query(obj, 'AAAA')
	for ans in ansAAAA:
		print "[-]", ans
except dns.resolver.NoAnswer:
	print "No se encontró información sobre direcciones IPv6"
	ansAAAA = []
except dns.exception.Timeout:
	if not socket.has_ipv6:
		print "No se encontró información sobre direcciones IPv6"
		ansAAAA = []
except dns.exception.DNSException as e:
	print "No se encontró información sobre direcciones IPv6"
	ansAAAA = []

print "**********************"

print "Información sobre registros SOA:"
for ans in ansSOA:
	print "[-]", ans

print "**********************"

print "Información sobre registros de texto:"
for ans in ansTXT:
	print "[-]", ans

print "********************** \n"
