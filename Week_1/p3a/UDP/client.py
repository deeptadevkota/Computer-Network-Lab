import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = "connecting"
bytesdata = str.encode(data)

client.sendto(bytesdata,("localhost",9999))

print(client.recvfrom(1024)[0].decode())

while True:

    query = input("You: ")
    bytesdata = str.encode(query)

    client.sendto(bytesdata,("localhost",9999))

    print("Server: ",client.recv(1024).decode())
    if query=="END":
        break
