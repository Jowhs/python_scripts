#!/usr/bin/python

class nombre(object):
	def __init__(self, apellido, altura):
		self.apellido = apellido
		self.altura = altura
yo=nombre("Name", 185)

print yo.apellido, yo.altura
