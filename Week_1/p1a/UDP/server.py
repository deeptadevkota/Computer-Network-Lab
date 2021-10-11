import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("localhost",9999))

print("Waiting for client")

while True:
    data, address = server.recvfrom(1024)

    print("Connected to client: ", address)

    message = "Welcome to my server"
    bytesdate = message.encode()
    
    server.sendto(bytesdate, address)