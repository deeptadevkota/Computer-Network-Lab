import socket
import threading

handle = input("Enter a handle: ")

client = socket.socket()
client.connect(("localhost",9999))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'Enter a handle: ':
                client.send(bytes(handle,'utf-8'))
            else:
                print(message)
        except:
            print('Error')
            client.close()
            break

def write():
    while True:
        message = input()
        client.send(bytes(message,'utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()