import socket
from datetime import date

server = socket.socket()

server.bind(('localhost',9999))

server.listen(1)
print('Waiting for client')

client, address = server.accept()

print("Connected to client: ", address)
client.send(bytes("Welcome to server chat room, enter 'END' to leave the chat room!",'utf-8'))

while True:

    q = client.recv(1024).decode()
    print("Client: " , q) 

    answer = input("Response: ")
    client.send(bytes(answer,'utf-8'))

    if q=="END":
        break

client.close()



