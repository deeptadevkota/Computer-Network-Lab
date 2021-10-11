import socket

client = socket.socket()

client.connect(('localhost',9999))

client.send(bytes('What is today\'s date?','utf-8'))

print(client.recv(1024).decode())

