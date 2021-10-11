import socket
import threading

server = socket.socket()
server.bind(('localhost',9999))
server.listen(20)
print('Waiting for client')

clients = []
handles = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handleConnections(client):
    while True:
        try:
            message = client.recv(1024)
            message = message.decode()
            index = clients.index(client)
            handle = handles[index]
            broadcast(bytes(handle+ ': '+ message,'utf-8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            handle = handles[index]
            broadcast(bytes(handle+' left the chat room','utf-8'))
            handles.remove(handle)
            break

def receive():
    while True:
        client, address = server.accept()
        print('Connected with client: ', address)

        client.send(bytes('Enter a handle: ','utf-8'))
        handle = client.recv(1024).decode()
        clients.append(client)
        handles.append(handle)

        print('Handle of connected client: ',handle)

        broadcast(bytes(handle+' joined the chat room!','utf-8'))

        thread = threading.Thread(target=handleConnections,args=(client,))
        thread.start()
        

receive()

