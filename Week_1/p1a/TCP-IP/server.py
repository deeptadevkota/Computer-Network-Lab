import socket

server = socket.socket()

server.bind(('localhost',9999))

server.listen(1)
print('Waiting for client')

while True:
    client, address = server.accept()
    print("Connected to client: ", address)

    client.send(bytes("Welcome to my server!",'utf-8'))

    client.close()


