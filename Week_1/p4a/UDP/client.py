import socket
import threading

handle = input("Enter a handle: ")
host = ("localhost",9999)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(bytes(handle,'utf-8'),host)

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'Enter a handle: ':
                client.sendto(bytes(handle,'utf-8'),host)
            else:
                print(message)
        except:
            print('Error')
            break

def write():
    while True:
        message = input()
        client.sendto(bytes(message,'utf-8'),host)

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()