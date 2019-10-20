import socket
import sys
from thread import *
from subprocess import Popen
from subprocess import PIPE

ip = "0.0.0.0"
port = 54555
max_conn = 5
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((ip, port))
except socket.error as msg:
    print "Bind failed, Error Code: " + str(msg[0]) + "Message: " + str(msg[1])
    sys.exit()

server.listen(max_conn)
print "[*] Waiting for connections on %s:%d" % (ip, port)

def client_thread(conn):
    conn.send("ACK")
    while True:
        data = conn.recv(4096)
        reply = "OK... " + data
        if not data:
            break
        print reply # la respuesta se muestra en el servidor
        #conn.sendall(reply) --> La respuesta se muestra en el cliente
    conn.close()

while 1:
    conn, addr = server.accept()
    print "Connection established with " + addr[0] + ":" + str(addr[1])
    start_new_thread(client_thread, (conn,))
server.close()
