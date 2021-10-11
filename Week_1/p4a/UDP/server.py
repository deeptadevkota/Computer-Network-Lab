import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost",9999))

print("Waiting for client")

clients = []
handles = []

def broadcast(message):
    for client in clients:
        server.sendto(message,client)

def handleConnectionClient(client,data):
    try:
        message = data.decode()
        index = clients.index(client)
        handle = handles[index]
        broadcast(bytes(handle+ ': '+ message,'utf-8'))
    except:
        index = clients.index(client)
        clients.remove(client)
        handle = handles[index]
        broadcast(bytes(handle+' left the chat room','utf-8'))
        handles.remove(handle)

def receive():
    while True:
        data, address = server.recvfrom(1024)

        if address not in clients:
            message = data.decode()
            print('Connected with client: ', address)
            clients.append(address)
            handles.append(message)
            print('Handle of connected client: ',message)
            broadcast(bytes(message+' joined the chat room!','utf-8'))
            thread = threading.Thread(target=handleConnectionClient,args=(address,data,))
            thread.start()
        else:
            handleConnectionClient(address,data)

receive()