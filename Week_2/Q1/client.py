import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost", 8000))


request='GET /index.html HTTP/1.0'    
client.sendall(request.encode())

response=client.recv(1024).decode()
print(response)

client.close()