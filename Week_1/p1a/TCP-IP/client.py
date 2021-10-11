import socket

client = socket.socket()

client.connect(('localhost',9999))

print(client.recv(1024).decode())

