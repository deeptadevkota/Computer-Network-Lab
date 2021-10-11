import socket
from datetime import date

server = socket.socket()

server.bind(('localhost',9999))

server.listen(1)
print('Waiting for client')

while True:
    client, address = server.accept()
    
    print("Connected to client: ", address)

    print("Query: " , client.recv(1024).decode()) 
    
    today = date.today().strftime("%d / %m / %Y")
    data = "Welcome, today\'s date is : " + today
    client.send(bytes(data,'utf-8'))

    client.close()


