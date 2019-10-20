# -*- coding: utf-8 -*-

import os
import time

if os.name == "NT": # si el sistema es windows NT que aplique 'dir' en la siguiente linea
	command = "dir"
else:
	command = "ls -l" # si no es windows será unix, por tanto que liste con 'ls -l'

print "==================================="
print os.system(command) # le damos la instrucción para que ejecute 'ls -l'
for file in os.listdir("."): # nos lista el contenido del directorio completo
	print file

print "==================================="
cwd = os.getcwd() # nos devuelve el directorio actual 
print "1", cwd
os.chdir("chee") # equivale al comando cd, para cambiar de directorio
print "2", os.getcwd()
os.chdir(os.pardir) # equivale al comando cd .., volver un directorio hacia atrás
print "3", os.getcwd()

print "==================================="
os.makedirs("test/testing") # crea directorios
fp = open("test/testing/testfile", "w") # creamos un fichero
fp.write("text inside the new file") # el texto dentro del nuevo archivo
fp.close()
print "Directorio y fichero creados..."
