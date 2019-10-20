import socket

server = "192.168.235.145"
port = 54555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server, port))
client.sendall("Hello World".encode('UTF-8'))
res = client.recv(4096)
print res.decode('UTF-8')
client.close()
