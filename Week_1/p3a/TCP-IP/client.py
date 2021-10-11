import socket

client = socket.socket()

client.connect(('localhost',9999))

print(client.recv(1024).decode())

while True:
    query = input("You: ")
    client.send(bytes(query,'utf-8'))
    print("Server: ",client.recv(1024).decode())
    if query=="END":
        break

