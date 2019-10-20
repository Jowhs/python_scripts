# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE # permite enviar órdenes directas al SO e interactuar con él

for ip in range(128,140): # crea un barrido entre las máquinas de 1 al 10 del rango indicado abajo ..192.168.235..
	ipAddress = "192.168.235." + str(ip)
	print "Haciendo ping ... %s " %(ipAddress)
	subprocess = Popen(['bin/ping', '-c 1 ', ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE) # hace un ping con Popen
	stdout, stderr = subprocess.communicate(input=None) # comunicamos y nos da el flujo de salida y el de error
	if "bytes from" in stdout: # si aparece la frase 'bytes from' habrá comunicación, la máquina estará activa
		print "La dirección IP %s ha respondido con un ECHO REPLY" %(stdout.split()[1])
		with open("ips.txt", "a") as myfile: # Abrimos el archivo 'ips.txt' en modo append y escribimos abajo el número de la dirección IP
			myfile.write[stdout.split()[1]+'\n']
