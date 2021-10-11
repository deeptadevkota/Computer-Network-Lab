import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("localhost",9999))

print("Waiting for client")

data, address = server.recvfrom(1024)

print("Connected to client: ", address)

message = "Welcome to server chat room, enter 'END' to leave the chat room!"
bytesdate = str.encode(message)
server.sendto(bytesdate, address)

while True:

    data, address = server.recvfrom(1024)
    query = data.decode()
    print("Client: ",query)

    reponse = input("Response: ")
    bytesdate = str.encode(reponse)
    server.sendto(bytesdate, address)

    if query == "END":
        break