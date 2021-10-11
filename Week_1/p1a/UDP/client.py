import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = "connecting"
bytesdata = str.encode(data)

client.sendto(bytesdata,("localhost",9999))

print(client.recvfrom(1024)[0].decode())
